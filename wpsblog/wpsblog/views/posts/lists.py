from django.shortcuts import render


def lists(request):
    return render(request,
        "posts/lists.html",
        {"list" : "haha"}
        )
