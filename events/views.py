from django.shortcuts import render
from django.views.generic import ListView, CreateView
from events.models import Event
from events.forms import EventForm


class EventsListView(ListView):
    model = Event
    # queryset = Event.objects.all().order_by('-date')
    template_name = "events.html"


class CreateEventView(CreateView):
    template_name = "create_event.html"
    form_class = EventForm
    model = Event
