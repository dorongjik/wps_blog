from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username = username,
            email = email,
            password = password,
        )

        return redirect(reverse("auth:login"))

    else:
        return render(request,
        "auth/signup.html",
        )