from django.shortcuts import render
from django.views.generic import ListView
from models import Event


class EventsListView(ListView):
    model = Event
    # queryset = Event.objects.all().order_by('-date')
    template_name = "events.html"
