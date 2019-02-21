from django.db import models
from django.utils import timezone


class Message(models.Model):
    text = models.TextField()
    author_name = models.CharField(max_length=100)
    author_mail = models.EmailField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {}".format(self.author_name, self.post_date)
