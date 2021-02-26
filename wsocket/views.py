from django.shortcuts import render


def room(request):
    return render(request, 'socket/room.html', {
        'room_name': "name"
    })
