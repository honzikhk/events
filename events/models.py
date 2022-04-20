from django.db import models
from django.shortcuts import resolve_url


class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    eated = models.IntegerField()
    poo = models.BooleanField(default=False, null=True, blank=True)
    note = models.CharField(max_length=200)

    def get_absolute_url(self):
        return resolve_url('events')

