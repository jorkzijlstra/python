from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
import uuid
from uuid import UUID
from backoffice.common.utils import string_to_uuid
from pprint import pprint
from backoffice.common.enumerations import JobBranches, Organisations
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Organisation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    titel = models.CharField(max_length=250)
    permalink = models.SlugField(null = False, blank = False, editable=False)
    dateCreated = models.DateTimeField(auto_now=True, editable = False)
    dateUpdated = models.DateTimeField(null=True, blank=True, editable = False)
    
    def __str__(self):
        return str(self.titel)
    
    def save(self, *args, **kwargs):
        if not self.permalink:
            self.permaLink = slugify(self.titel)
        
        super(Organisation, self).save()

class UserWithOrganisation(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    organisation = models.CharField(max_length=8, choices=Organisations.choices())
    
    def __str__(self):
        return str(self.organisation)

class Vacature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    slug = models.SlugField(null=True, blank=True, editable=False)
    permalink = models.SlugField(null = False, blank = False, editable=False)
    
    organisation = models.CharField(max_length=8, choices=Organisations.choices())

    dateCreated = models.DateTimeField(auto_now=True, editable = False)
    dateUpdated = models.DateTimeField(null=True, blank=True, editable = False)
    datePublished = models.DateTimeField(null=True, blank=True, editable = False)

    def is_published(self):
        return self.datePublished is not None
   
    def __str__(self):
        return str(self.id)
    
    def content(self):
        return VacatureContent.objects.get(pk = string_to_uuid(str(self.id)))
    
    def features(self):
        return VacatureFeatures.objects.get(pk = string_to_uuid(str(self.id)))
    
    is_published.boolean = True
    is_published.short_description = "Gepubliceerd?"

class VacatureContent(models.Model):
    titel = models.CharField(max_length=250)
    omschrijving = models.TextField()
    vacatureId = models.OneToOneField(Vacature, default=uuid.uuid4, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    
    def save(self, *args, **kwargs):
        vacature = Vacature.objects.get(pk = string_to_uuid(str(self.vacatureId)))
        vacature.slug = slugify(self.titel)
        
        if not vacature.permalink:
            vacature.permalink = slugify(self.titel)
        
        vacature.save()
            
        super(VacatureContent, self).save()

class VacatureFeatures(models.Model):
    code = models.CharField(max_length=8),
    #regions =  models.CharField(max_length=10, choices=JOBBRANCHES)
    jobBranches = models.CharField(max_length=8, choices=JobBranches.choices())
    vacatureId = models.OneToOneField(Vacature, default=uuid.uuid4, on_delete=models.CASCADE, primary_key=True, parent_link=True)

