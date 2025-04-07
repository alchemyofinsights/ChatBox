from django import forms
from .models import Chatbox

class ChatboxForm(forms.ModelForm):
    class Meta:
        model = Chatbox
        fields = ['name', 'password']

from django import forms

class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Chatbox
        fields = ['name', 'password']
