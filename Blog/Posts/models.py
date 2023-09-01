from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'<Post: {self.title}> <id: {self.pk}>'
