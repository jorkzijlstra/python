from __future__ import unicode_literals

import uuid

from django.db import models


class Vacature(models.Model):
    slug = models.SlugField(primary_key=True)
    titel = models.CharField(max_length=250)
    omschrijving = models.TextField()
    dateCreated = models.DateTimeField(auto_now=True, editable = False)