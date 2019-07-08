from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    link = models.URLField()
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.link
