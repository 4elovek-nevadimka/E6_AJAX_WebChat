from django.urls import path

from . import views
from .api.views import RoomListView, RoomDeleteView, RoomUpdateView, RoomDetailView, RoomCreateView
from .views import AllRoomsView, AllUsersView, MyRoomsView, MyProfileView, update_firstname

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('my-profile/', MyProfileView.as_view(), name='my_profile'),
    path('my-rooms/', MyRoomsView.as_view(), name='my_rooms'),
    path('all-rooms/', AllRoomsView.as_view(), name='all_rooms'),
    path('all-users/', AllUsersView.as_view(), name='all_users'),

    path('update_firstname/', update_firstname, name='update_firstname'),

    path('room/', RoomListView.as_view()),
    path('room/create/', RoomCreateView.as_view()),
    path('room/<pk>', RoomDetailView.as_view()),
    path('room/<pk>/update/', RoomUpdateView.as_view()),
    path('room/<pk>/delete/', RoomDeleteView.as_view())
]
