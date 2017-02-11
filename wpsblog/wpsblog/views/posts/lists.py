from django.shortcuts import render
from wpsblog.models import Post
from wpsblog.models import Comment

def lists(request):
    return render(request,
        "posts/lists.html",
        {
            "posts": Post.objects.public, # 여기의 posts가 template으로 날아감
        },
        )
