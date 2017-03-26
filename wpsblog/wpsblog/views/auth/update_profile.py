from django.shortcuts import redirect
from django.contrib.auth.models import User

def update_profile(request):
    User = request.user

    User.first_name = request.POST.get("first_name")
    User.username = request.POST.get("username")
    User.email = request.POST.get("email")
    User.last_name = request.POST.get("last_name")
    User.password = request.POST.get("password")

    User.save() # 요놈을 꼭 해주십다!

    return redirect(profile)
    