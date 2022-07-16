from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from chat.models import UserProfile, Room


class MyProfileView(LoginRequiredMixin, DetailView):
    template_name = 'chat/my_profile.html'
    model = UserProfile

    def get_object(self):
        return get_object_or_404(UserProfile, id=self.request.user.id)


class MyRoomsView(LoginRequiredMixin, ListView):
    template_name = 'chat/my_rooms.html'
    model = Room
    context_object_name = 'my_rooms_list'
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


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


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
