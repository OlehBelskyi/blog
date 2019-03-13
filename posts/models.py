from django.db import models
from users.models import User


# Create your models here.
class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(max_length=2000, verbose_name="Content")
    author = models.CharField(max_length=40, verbose_name="Author", default="Ghost")
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
