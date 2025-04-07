from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Chatbox
from django.http import HttpResponse
from .forms import CreateRoomForm  # create this form below

def home(request):
    return render(request, 'chat/home.html')  # Make sure this template exists


def create_room(request):
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect('chat_room', room_name=room.name)
    else:
        form = CreateRoomForm()
    return render(request, 'chat/create_room.html', {'form': form})



def join_room(request):
    if request.method == "POST":
        username = request.POST.get("username")
        room_name = request.POST.get("room_name")
        password = request.POST.get("password")

        # Try to fetch a room that matches both name AND password
        room = Chatbox.objects.filter(name=room_name, password=password).first()

        if room:
            request.session['username'] = username  # Set it before redirect
            return redirect("chat_room", room_name=room_name)

        else:
            return HttpResponse("Room not found or incorrect password.")
    
    return render(request, "join.html")

def chat_room(request, room_name):
    username = request.session.get('username', 'Anonymous')
    return render(request, 'chat/room.html', {
        'username': username,
        'room_name': room_name,
    })
