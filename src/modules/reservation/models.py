from django.contrib.auth.models import User
from django.db import models


class UserName(models.Model):
    """Generate username"""
    id = models.AutoField(primary_key=True)


class UserProfile(models.Model):
    """Additional user data"""
    user = models.OneToOneField(User)
    credit = models.DecimalField(max_digits=5, decimal_places=2, default=0)


class Coach(models.Model):
    """Event coach"""
    user = models.ForeignKey(User, blank=True, null=True)
    page_link = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)


class Event(models.Model):
    """Event"""
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(`)
    time = models.TimeField()
    max_participants = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    coach = models.ForeignKey(Coach)
    participants = models.ManyToManyField(User, through='EventParticipants')

    def __unicode__(self):
        return "%s (%s %s)" % (self.title, self.date, self.time)


class EventParticipants(models.Model):
    """Event participants"""
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    date_joined = models.DateTimeField(auto_now_add=True)
    prepaid = models.BooleanField(default=False)
