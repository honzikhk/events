from django.db import models
from django.shortcuts import resolve_url


class Event(models.Model):
    POO_YES = "Yes"
    POO_NO = "No"

    POO_CHOICES = (
        (POO_YES, "Yes"),
        (POO_NO, "No"),
    )

    date = models.DateField()
    time = models.TimeField()
    eated = models.IntegerField()
    poo = models.CharField(choices=POO_CHOICES, default="No", max_length=5)
    note = models.TextField(null=True, blank=True, max_length=1000)

    def get_absolute_url(self):
        return resolve_url('create_event')

