from django.shortcuts import render
from django.shortcuts import redirect
from wpsblog.models import Post


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    image = request.FILES.get("image")

    post = Post.objects.create(
            title=title,
            content=content,
            image=image,
            user=request.user,
            )

    return redirect(post)