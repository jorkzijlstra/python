from __future__ import unicode_literals

from django.db import models
import uuid

class Vacature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField()
    titel = models.CharField(max_length=250)
    omschrijving = models.TextField()
    dateCreated = models.DateTimeField(auto_now=True, editable = False)
