from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .forms import RoomForm
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


class RoomCreateView(LoginRequiredMixin, CreateView):
    form_class = RoomForm
    template_name = 'chat/room_create.html'

    def form_valid(self, form):
        form.instance.author = UserProfile.objects.filter(user=self.request.user).first()
        return super().form_valid(form)


@login_required
def chat_room(request, room_id):
    # cur_room = Room.objects.get(pk=room_id)
    username = request.user.username

    return render(request, 'chat/chat-room.html', {'room_id': room_id, 'username': username, })

    # return render(request, 'chat/chat-room.html',
    #               {'room_name': room_name, 'username': username, 'messages': cur_room.messages[0:25]})


def update_firstname(request):
    if request.method == 'POST':
        userprofile = UserProfile.objects.get(pk=request.POST['user_profile_id'])
        userprofile.user.first_name = request.POST['first_name']
        userprofile.user.save()
    return HttpResponse('update successful')
