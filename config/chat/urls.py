from django.urls import path

from . import views
# from .api.views import RoomListView, RoomDeleteView, RoomUpdateView, RoomDetailView, RoomCreateView
from .views import AllRoomsView, AllUsersView, MyRoomsView, MyProfileView, update_firstname, RoomCreateView

urlpatterns = [
    path('<int:room_id>/', views.chat_room, name='room'),

    path('account/my-profile/', MyProfileView.as_view(), name='my_profile'),
    path('account/my-rooms/', MyRoomsView.as_view(), name='my_rooms'),
    path('account/all-rooms/', AllRoomsView.as_view(), name='all_rooms'),
    path('account/all-users/', AllUsersView.as_view(), name='all_users'),

    path('update_firstname/', update_firstname, name='update_firstname'),

    path('room/create/', RoomCreateView.as_view(), name='room_create'),

    # path('room/', RoomListView.as_view()),
    # path('room/create/', RoomCreateView.as_view()),
    # path('room/<pk>', RoomDetailView.as_view()),
    # path('room/<pk>/update/', RoomUpdateView.as_view()),
    # path('room/<pk>/delete/', RoomDeleteView.as_view())
]
