from django.db import models

class Comment(models.Model):

    post = models.ForeignKey("Post") # M:N 관계를 명시, 여기서는 1:N

    content = models.TextField()

    def __str__(self):
        return self.content