from .models import Rooms
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def AddRooms(request):
    # request type check
    if request.method == 'POST':
        # room object
        room_obj = Rooms()
        room_obj.room_number=request.POST.get('room_number')
        room_obj.price=request.POST.get('price')
        room_obj.availability=request.POST.get('availability')
        room_obj.sea_view=request.POST.get('sea_view')
        room_obj.pool_view=request.POST.get('pool_view')
        # Create that backend entry
        room_obj.save()
        data = {"results": True}
        return JsonResponse(data)

# get request /get_room/room_number
def GetRoom(request, room_id):
    room = get_object_or_404(Rooms, room_number=room_id)
    data = {"results": {
        "room_number": room.room_number,
        "price": room.price,
        "availability": room.availability,
        "sea_view": room.sea_view,
        "pool_view": room.pool_view,
    }}
    return JsonResponse(data)

# return the whole list of rooms
def getRoomsList(request):
    pass