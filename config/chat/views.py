from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import UserProfile, Room


class MyProfileView(LoginRequiredMixin, DetailView):
    template_name = 'chat/my_profile.html'
    model = UserProfile

    def get_object(self, **kwargs):
        return get_object_or_404(UserProfile, user=self.request.user)


class MyRoomsView(LoginRequiredMixin, ListView):
    template_name = 'chat/my_rooms.html'
    model = Room
    context_object_name = 'my_rooms_list'
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset().filter(author__user=self.request.user)


class AllRoomsView(LoginRequiredMixin, ListView):
    template_name = 'chat/all_rooms.html'
    model = Room
    context_object_name = 'all_rooms_list'
    ordering = ['-id']


class AllUsersView(LoginRequiredMixin, ListView):
    template_name = 'chat/all_users.html'
    model = UserProfile
    context_object_name = 'all_users_list'
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset().exclude(user=self.request.user)


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


def chat_room(request, room_name):
    # cur_room = Room.objects.filter(pk=room_id).first()
    username = request.user.username

    return render(request, 'chat/chat-room.html',
                  {'room_name': room_name, 'username': username, })

    # return render(request, 'chat/chat-room.html',
    #               {'room_name': room_name, 'username': username, 'messages': cur_room.messages[0:25]})


def update_firstname(request):
    if request.method == 'POST':
        userprofile = UserProfile.objects.get(pk=request.POST['user_profile_id'])
        userprofile.user.first_name = request.POST['first_name']
        userprofile.user.save()
    return HttpResponse('update successful')
