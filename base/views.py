from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from .models import Room
from .forms import RoomForm
# rooms = [
#     {
#         'id':1,
#      'name':'Lets learn python',
#      },
#     {
#         'id':2,
#         'name':'Lets learn django',
#      },
#     {
#         'id':3,
#         'name':'Lets learn react',
#      },
#     {
#         'id':4,
#         'name':'Lets learn angular',
#      },
#     {
#         'id':5,
#         'name':'Lets learn vue',
#      },
#   ]
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)  
    context = {'room':room}
    return render(request,'base/room.html',context)

def createRoom(request):
    form = RoomForm()
    context = {'form' : form}
    return render(request,'base/room_form.html',context)
