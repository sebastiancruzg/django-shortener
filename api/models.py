import uuid

from django.db import models

# Create your models here.


class Urls(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    original_url = models.CharField(unique=True, max_length=255)
    short_url = models.CharField
    created_at = models.DateTimeField(auto_now_add=True)
