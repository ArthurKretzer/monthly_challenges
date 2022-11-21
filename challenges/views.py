from django.shortcuts import render
from django.http import (Http404, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Eat no meat for the entire month!",
    "december": None
}
# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month.</h1>")

    redirect_month = months[month]
    # /challenge/<redirect_month:str>
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # the month input is here because of the place holder set on urls.py with
    # the exact same name
    try:
        challenge_text = monthly_challenges[month]
        # it is a good practice to create a folder inside templates folder
        #  with the name of your app so you don't eventually come with same
        # file names, which would cause conflict.
        # since returning a template is frequent, django has the render
        # function which renders the template to string and sends it through a
        #  http response.
        # render and render to string have a third input that is a dictionary
        #  containing key-value pairs to be interpolated into the template
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        # searches for a 404.html file on templates
        raise Http404()
