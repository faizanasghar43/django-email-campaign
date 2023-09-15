from django.contrib.auth.models import User
from django.db import models
from training_synares.models import BaseModelClass


class Campaign(BaseModelClass):
    title = models.TextField(max_length=254)
    description = models.TextField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Campaign: \n {self.title} \n {self.description} \n {self.user} '