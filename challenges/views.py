from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january"  : "Eat no meat for the entire month!",
    "february" : "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may" : "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july"  : "Eat no meat for the entire month!",
    "august" : "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Eat no meat for the entire month!",
    "december" : "Walk for at least 20 minutes every day!"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month.")

    redirect_month = months[month]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/<redirect_month:str>
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # the month input is here because of the place holder set on urls.py with the exact same name
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
