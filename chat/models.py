from django.db import models

class Chatbox(models.Model):
    name = models.CharField(max_length=100, unique=True)  # enforce uniqueness
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
