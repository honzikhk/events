from django.urls import path
from events.views import CreateEventView, AllEventView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", CreateEventView.as_view(), name="create_event"),
    path("all/", AllEventView.as_view(), name="allevents"),
    path("chart/", views.index, name="index"),
]

urlpatterns += staticfiles_urlpatterns()

