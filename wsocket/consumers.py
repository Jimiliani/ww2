import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer

from wsocket.models import FakeUser, GameField, GameCell

waiting_room = []

channel_layer = get_channel_layer()


class SocketConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(json.dumps({
            'event': 'connect'
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if data['event'] == 'registration':
            user = FakeUser.objects.create(username=data['nickname'], channel_name=self.channel_name)
            self.user = user
        elif data['event'] == 'ready':
            if len(waiting_room) >= 1:
                user_to_connect = waiting_room.pop()
                self.user.enemy = user_to_connect
                self.user.country = 'USA'
                self.user.save()
                user_to_connect.country = 'Japan'
                user_to_connect.save()
                self.send(json.dumps({
                    'event': 'ready',
                    'other_name': user_to_connect.nickname,
                    'first_move': False
                }))
                async_to_sync(channel_layer.send)(user_to_connect.channel_name, json.dumps({
                    'event': 'ready',
                    'other_name': self.user.nickname,
                    'first_move': True
                }))
            else:
                waiting_room.append(self.user)

            field = data['field']
            field_ = GameField.objects.create()
            self.user.game_field = field_
            for index1, row in enumerate(field):
                for index2, value in enumerate(row):
                    if value == 0:
                        cell = GameCell.objects.create(row=index1, column=index2, cell_type='0')
                    else:
                        cell = GameCell.objects.create(row=index1, column=index2, cell_type='1')
                    field_.cells.add(cell)
        elif data['event'] == 'fire':
            cell = self.user.enemy.field.cells.get(row=data['row'], column=data['col'])
            if cell.cell_type == '1':
                hit = True
            else:
                hit = False
            finish = False
            if self.user.field.cells.filter(cell_type='1').count() != 0:
                finish = True
            self.send(json.dumps({
                'event': 'fire',
                'row': data['row'],
                'col': data['col'],
                'hit': hit,
                'finish': 1 if finish else 0
            }))
            async_to_sync(channel_layer.send)(self.user.enemy.channel_name, json.dumps({
                'event': 'fire',
                'row': data['row'],
                'col': data['col'],
                'hit': hit,
                'finish': -1 if finish else 0
            }))
            cell.cell_type = '-1'
            cell.save()
        else:
            self.send(json.dumps({
                'event': 'unknown_event',
            }))
