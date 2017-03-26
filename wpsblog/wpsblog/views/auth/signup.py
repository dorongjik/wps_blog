from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username = username,
            first_name = first_name,
            password = password,
        )

        return redirect(reverse("auth:login"))

    else:
        return render(request,
        "auth/signup.html",
        )