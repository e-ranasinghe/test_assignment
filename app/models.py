from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    # user = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField()
