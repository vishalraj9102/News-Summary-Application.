from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SavedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_articles')
    title = models.CharField(max_length=512)
    content = models.TextField()
    url = models.URLField(max_length=1024)
    source = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
