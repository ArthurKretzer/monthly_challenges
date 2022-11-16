from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    # the month input is here because of the place holder set on urls.py with the exact same name

    challenge_name = None
    if month == 'january':
        challenge_name = "Eat no meat for the entire month!"
    elif month == 'february':
        challenge_name = "Walk for at least 20 minutes every day!"
    elif month == 'march':
        challenge_name = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_name)
