from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
import uuid

class Vacature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    slug = models.SlugField(null = True, blank = True, editable=False)
    titel = models.CharField(max_length=250)
    omschrijving = models.TextField()
    dateCreated = models.DateTimeField(auto_now=True, editable = False)
    dateUpdated = models.DateTimeField(null=True, blank=True, editable = False)

    def save(self):
        if not self.slug:
            self.slug = slugify(self.titel)

        super(Vacature, self).save()
        
'''
class VacatureContent(models.Model):
    titel = models.CharField(max_length=250)
    omschrijving = models.TextField()
    vacatureId = models.OneToOneField(Vacature, default=uuid.uuid4, on_delete=models.CASCADE, primary_key=True)
'''