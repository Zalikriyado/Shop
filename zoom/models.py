from django.db import models
from user.models import User

class Post(models.Model):
    title = models.CharField(max_length=256)
    desc = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='post/')
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=512)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')