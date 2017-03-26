from django.shortcuts import render
from wpsblog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def step2(request):
    return render(request,
        "checkout/step2.html",
        {
            "post" : Post.objects.get(id=request.POST.get("post_id")),
            "designtext" : request.POST.get("designtext"),
            "email" : request.POST.get("email"),
            "phone" : request.POST.get("phone"),
            "demands" : request.POST.get("demands"),
            "paymentMethod" :request.POST.get("paymentMethod"),
        },
    )
# detal.html에서 form 태그로 부르자