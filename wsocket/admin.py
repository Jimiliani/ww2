from django.contrib import admin
from django.contrib.auth.models import Group, User

from wsocket.models import FakeUser, GameField, GameCell

admin.site.register(FakeUser)
admin.site.register(GameField)
admin.site.register(GameCell)
admin.site.unregister(User)
admin.site.unregister(Group)
