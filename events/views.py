from django.shortcuts import render
from django.views.generic import ListView, CreateView
from events.models import Event
from events.forms import EventForm

#
# class EventsListView(ListView):
#     model = Event
#     template_name = "events.html"


class CreateEventView(CreateView):
    template_name = "events.html"
    form_class = EventForm
    model = Event

    def get_context_data(self, *args, **kwargs):
        context = super(CreateEventView, self).get_context_data(**kwargs)
        context.update({
            "last_ten_events": Event.objects.all(limit=10),
            'all_events': Event.objects.all().order_by("-id"),
        })
        return context
