from django.shortcuts import render


def index(request):
    """View function for the home page of the site."""

    num_drivers = 0
    num_cars = 0
    num_manufacturers = 9

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1,
    }

    return render(request, "todo/index.html", context=context)

