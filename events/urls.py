from django.urls import path
from events.views import CreateEventView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", CreateEventView.as_view(), name="create_event"),
]

urlpatterns += staticfiles_urlpatterns()

