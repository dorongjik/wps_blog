from django.shortcuts import render
from wpsblog.models import Post

def lists(request):
    return render(request,
        "posts/lists.html",
        {
            "posts": Post.objects.filter(is_public=True) # 여기의 posts가 template으로 날아감
        },
        )
