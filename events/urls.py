from django.urls import path
from events.views import CreateEventView, AllEventView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", CreateEventView.as_view(), name="create_event"),
    path("all/", AllEventView.as_view(), name="allevents"),
]

urlpatterns += staticfiles_urlpatterns()

