from django.shortcuts import redirect
from wpsblog.models import Post

def create_comment(request, post_id):
    content = request.POST.get("content")
    post = Post.objects.get(id=post_id)

    comment = post.comment_set.create(
        content = content,
    )

    return redirect(comment)

def delete_comment(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    comment.delete()
    
    return redirect(post)
