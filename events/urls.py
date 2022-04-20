from django.urls import path
from events.views import EventsListView, CreateEventView

urlpatterns = (
    path("", EventsListView.as_view(), name="events"),
    path("create/", CreateEventView.as_view(), name="create_event")
)
