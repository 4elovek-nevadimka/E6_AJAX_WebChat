from django.urls import path

from . import views
from .views import AllRoomsView, AllUsersView, MyRoomsView, MyProfileView

urlpatterns = [
    # path('', views.index, name='index'),
    # path('room/<str:room_name>/', views.room, name='room'),
    path('my-profile/', MyProfileView.as_view(), name='my_profile'),
    path('my-rooms/', MyRoomsView.as_view(), name='my_rooms'),
    path('all-rooms/', AllRoomsView.as_view(), name='all_rooms'),
    path('all-users/', AllUsersView.as_view(), name='all_users'),
]
