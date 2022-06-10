import datetime

from django.shortcuts import render
from django.views.generic import CreateView, ListView
from events.models import Event
from events.forms import EventForm


class CreateEventView(CreateView):
    template_name = "events.html"
    form_class = EventForm
    model = Event

    def get_context_data(self, *args, **kwargs):
        context = super(CreateEventView, self).get_context_data(**kwargs)
        today = datetime.datetime.today()
        events = Event.objects.all().filter(date=today)

        def count_food(eventsss):
            #events = Event.objects.all().filter(date=today)
            res = 0
            for event in events:
                res += event.eated
            return res

        context.update({
            "last_ten_events": Event.objects.all().order_by("-id")[:10],
            # "all_events": Event.objects.all().order_by("-id"),    # not used
            # "ate_today": Event.objects.all().filter(date=today),
            "ate_today": count_food(events)
        })
        return context


class AllEventView(ListView):
    template_name = "allevents.html"
    queryset = Event.objects.all()


def index(request):
    events = Event.objects.all()

    context = {
        "events": events
    }
    return render(request, "index.html", context)

