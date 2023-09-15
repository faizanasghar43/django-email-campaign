from django.db import models



class BaseModelClass(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    class Meta:
        abstract = True
