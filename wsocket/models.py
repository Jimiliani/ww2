from django.db import models


class FakeUser(models.Model):
    COUNTRY_CHOICES = [
        ('USA', 'Тупые пендосы'),
        ('Japan', 'Аниме')
    ]
    nickname = models.CharField(max_length=50)
    channel_name = models.CharField(max_length=50)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=5)
    room = models.OneToOneField('FakeUser', on_delete=models.CASCADE, related_name='enemy', null=True)
    game_field = models.OneToOneField('GameField', on_delete=models.CASCADE, null=True)


class GameField(models.Model):
    pass


class GameCell(models.Model):
    CELL_TYPE_CHOICES = [
        ('0', 'Вода'),
        ('1', 'Остров'),
        ('-1', 'Уничтожено')
    ]
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()
    game = models.ForeignKey(GameField, on_delete=models.CASCADE, related_name='cells')
    cell_type = models.CharField(choices=CELL_TYPE_CHOICES, max_length=2, default='0')
