from django.db import models
from wpsblog.models.post import Post

class Tag(models.Model):
    name = models.CharField(
        max_length=256,
    )

    post_set = models.ManyToManyField(Post)

    @property
    def full_name(self):
        return "#{name}".format(name=self.name)

    def __str__(self):
        return self.full_name
