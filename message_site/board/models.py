from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    author_name = models.CharField(max_length=100)
    author_mail = models.EmailField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {}".format(self.author_name, self.post_date)
