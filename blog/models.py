from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    """
    Blog post posted by user
    """
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User)


