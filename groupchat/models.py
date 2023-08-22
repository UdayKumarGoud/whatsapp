from django.db import models
# from django.contrib.auth.models import User
from users.models import AppUser

class Group(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    members = models.ManyToManyField(AppUser, related_name='groups')

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)