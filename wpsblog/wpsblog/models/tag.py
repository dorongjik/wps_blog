from django.db import models

class tag(models.Model):
    name = models.CharField(
        max_length=256,
    )

    @property
    def full_name(self):
        return "#{name}".format(name=self.name)

    def __str__(self):
        return self.full_name
