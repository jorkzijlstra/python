from __future__ import unicode_literals

from django.db import models
import uuid

class VacatureContent(models.Model):
    titel = models.CharField(max_length=250)
    omschrijving = models.TextField()
    
    def __str__(self):
        return self.titel

class Vacature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField()
    content =  models.ForeignKey(VacatureContent, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now=True, editable = False)
    dateCreated = models.DateTimeField(auto_now=False, editable = False)
    
