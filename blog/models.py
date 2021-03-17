from django.db import models

from django.contrib.auth.models import User
from django_quill.fields import QuillField



STATUS = (
    (0, "Draft"),
    (1, "Published"),
    (2, "Hidden")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    # content = models.TextField()
    content = QuillField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.CharField(max_length=256, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title}, {self.author}'
