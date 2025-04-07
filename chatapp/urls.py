"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # <- this is important
    path('', include('chat.urls')),  # or your app
]
"""

# project-level urls.py (usually Chatbox/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  # assuming 'chat' is your app name
    #path('home/', include('home.urls')),  # if you have a separate 'home' app
]
