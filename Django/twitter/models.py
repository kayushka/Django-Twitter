from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateTimeField(default=datetime.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    read = models.BooleanField(default=False)
    sender = models.ForeignKey(User, related_name="sent_messages", null=True, on_delete=models.SET_NULL)
    receiver = models.ForeignKey(User, related_name="received_messages", null=True, blank=True, on_delete=models.SET_NULL)

