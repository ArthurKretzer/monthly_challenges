from django.urls import path
from . import views

urlpatterns = [
    # this configures a place holder named month to dynamically set the route. We specify the type for the input. In that way we can set different routes.
    path("", views.index, name="index"), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
