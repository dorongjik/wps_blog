from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Comment(models.Model):

    post = models.ForeignKey("Post") # M:N 관계를 명시, 여기서는 1:N
    user = models.ForeignKey(User)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs={
                "post_id":self.post.id,
            },
        ) + "#comment-" + str(self.id) # 이 함수 정상적으로 작동 안 되는듯.
        