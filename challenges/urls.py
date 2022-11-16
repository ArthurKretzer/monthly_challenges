from django.urls import path
from . import views

urlpatterns = [
    # this configures the january route to execute the index function inside views file
    # path("january", views.index),
    # path("february", views.february),
    # this configures a place holder named month to dynamically set the route
    path("<month>", views.monthly_challenge),
]
