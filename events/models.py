from django.db import models


class Event(models.Model):
    date = models.DateTimeField()
    time = models.DateTimeField()
    eated = models.IntegerField()
    poo = models.BooleanField(default=False)
    note = models.CharField(max_length=200)
