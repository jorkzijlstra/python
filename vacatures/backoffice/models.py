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
    datePublished = models.DateTimeField(null=True, blank=True, editable = False)

    def save(self):
        if not self.slug:
            self.slug = slugify(self.titel)

        super(Vacature, self).save()
        
    def is_published(self):
        return self.datePublished is not None
    
    def __str__(self):
        return self.slug
    
    is_published.boolean = True
    is_published.short_description = "Gepubliceerd?"
   
'''
todo 
    - move properties to content
    - implement enumeration
    - fix one to one relation, should be in Vacature
    
class VacatureContent(models.Model):
    titel = models.CharField(max_length=250)
    omschrijving = models.TextField()
    vacatureId = models.OneToOneField(Vacature, default=uuid.uuid4, on_delete=models.CASCADE, primary_key=True)
    
class VacatureFeatures(models.Model):
    jobBranches = models.CharField(max_length=10, choices=JOBBRANCHES)
    vacatureId = models.OneToOneField(Vacature, default=uuid.uuid4, on_delete=models.CASCADE, primary_key=True)
'''