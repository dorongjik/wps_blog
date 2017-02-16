from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login

def login(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=username, email=email, password=password)

        if user:
            django_login(request, user)
            return redirect(reverse("home"))
        else:
            return redirect(reverse("auth:login"))

    # method : GET
    return render(request,
        "auth/login.html",
        )