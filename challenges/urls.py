from django.urls import path
from . import views

urlpatterns = [
    # this configures the january route to execute the index function inside views file
    path("january", views.index),
    path("february", views.february),
]

