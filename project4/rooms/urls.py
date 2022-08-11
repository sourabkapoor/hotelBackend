from django.urls import path
from . import views

urlpatterns = [
    path('add_rooms/', views.AddRooms, name="addRoom"),
    path('get_room/<int:room_id>/', views.GetRoom, name="getRoom")
]