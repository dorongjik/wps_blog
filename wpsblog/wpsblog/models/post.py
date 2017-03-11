from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class PostManager(models.Manager):
    def public(self):
        return self.filter(is_public=True)

    def ad(self):
        return self.filter(is_being_ad=True)
        

class Post(models.Model):

    objects = PostManager()

    user = models.ForeignKey(User)
    title = models.CharField(
        max_length=120,
    )

    content = models.TextField()
    phone = models.CharField(
        max_length=120,
    )
    image = models.ImageField(
        blank=True,
        null=True,
    )
    original_file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        blank=True,
        null=True,
    )
    price = models.PositiveIntegerField()
    
    is_public = models.BooleanField(
        default=True,
    )

    is_being_ad = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs = {
                "post_id" : self.id,
            }
        )

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return "http://placehold.it/350x150"
