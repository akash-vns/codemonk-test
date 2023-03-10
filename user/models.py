from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    """Abstract user model"""
    dob = models.DateField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)


class UserArticle(models.Model):
    """user articles/paragraphs"""
    content = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
