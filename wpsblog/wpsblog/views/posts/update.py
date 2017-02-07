from django.shortcuts import redirect
from wpsblog.models import Post

def update(request, post_id):
    post = Post.objects.get(id=post_id)

    post.title = request.POST.get("title")
    post.content = request.POST.get("content")

    post.save() # 요놈을 꼭 해주십다!

    return redirect(post)
    