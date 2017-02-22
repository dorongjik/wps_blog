from django.shortcuts import render
from django.shortcuts import redirect
from wpsblog.models import Post


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    image = request.FILES.get("image")
    price = request.POST.get("price")

    post = Post.objects.create(
            title=title,
            content=content,
            image=image,
            price=price,
            user=request.user,
            )

    return redirect(post)