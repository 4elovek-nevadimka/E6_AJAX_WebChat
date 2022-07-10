from django.contrib import admin

from chat.models import UserProfile, Message, Room

admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(Room)
