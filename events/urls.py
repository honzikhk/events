from django.urls import path
from events.views import CreateEventView

urlpatterns = (
    path("", CreateEventView.as_view(), name="create_event"),
)
