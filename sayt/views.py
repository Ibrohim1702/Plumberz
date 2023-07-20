from django.shortcuts import render

from sayt.models import Contact, Subscribe


# Create your views here.

def index(requests):
    ctx = {}
    if requests.POST:
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        date = requests.POST.get('date')
        email = requests.POST.get('email')
        Contact.objects.create(
            name=name, message=message, date=date, email=email
        )
    if requests.POST:
        email = requests.POST.get('email')
        Subscribe.objects.create(
            email=email
        )


        ctx = {

            "contact": contact,
            "email": email
        }
    return render(requests, "index.html", ctx)


def about(requests):
    ctx = {

    }
    return render(requests, "about.html", ctx)


def booking(requests):
    ctx = {

    }
    return render(requests, "booking.html", ctx)


def service(requests):
    ctx = {

    }
    return render(requests, "service.html", ctx)


def team(requests):
    ctx = {

    }
    return render(requests, "team.html", ctx)


def testimonial(requests):
    ctx = {

    }
    return render(requests, "testimonial.html", ctx)


def contact(requests):
    ctx = {

    }
    return render(requests, "contact.html", ctx)