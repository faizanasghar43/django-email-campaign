from django.contrib.auth.models import User
from django.db import models


class Scrappy(models.Model):
    url = models.URLField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emails = models.TextField(max_length=254)

    def __str__(self):
        return f"{self.user}"
