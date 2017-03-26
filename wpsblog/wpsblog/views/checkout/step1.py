from django.shortcuts import render
from wpsblog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def step1(request):
    return render(request,
        "checkout/step1.html",
        {
            "post" : Post.objects.get(id=request.POST.get("post_id")),
        },
    )
# detal.html에서 form 태그로 부르자