from django.contrib.auth.models import User
from django.db import models


class UserName(models.Model):
    """Generate username"""
    id = models.AutoField(primary_key=True)


class Event(models.Model):
    """Event"""
    title = models.CharField()
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    max_participants = models.IntegerField()


class Participant(models.Model):
    """Additional user data"""


class EventParticipants(models.Model):
    """Event participants"""
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
