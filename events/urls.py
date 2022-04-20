from django.urls import path
from events.views import EventsListView, CreateEventView

urlpatterns = (
    path("", CreateEventView.as_view(), name="create_event"),
)
