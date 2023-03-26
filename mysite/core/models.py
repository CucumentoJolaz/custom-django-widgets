from django.db import models
from django.urls import reverse
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name}'

class EventsBunch(models.Model):

    name = models.CharField(max_length=50)
    events = models.ManyToManyField(Event)

    def __str__(self):
        return f'{self.name}'
