from django.shortcuts import render
from django.core.paginator import Paginator
from wpsblog.models import Post
from wpsblog.models import Comment

def lists(request):
    page = request.GET.get("page", 1) # 기본값 1(첫 페이지)
    per = request.GET.get("per", 5) # 몇개씩 할 것인가

    paginator = Paginator(Post.objects.public(), per) # per개씩
    posts = paginator.page(page)

    return render(request,
        "posts/lists.html",
        {
            "posts": posts, # 여기의 posts가 template으로 날아감
        },
        )
