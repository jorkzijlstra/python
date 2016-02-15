from django.contrib import admin

from .models import Vacature

# Register your models here.
def publishToFrontOffice(backoffice_vacature):
    backoffice_vacature_content =  backoffice_vacature.content()
    
    try:
        existing_vacature = Vacature.objects.get(slug=backoffice_vacature.slug)
        existing_vacature.slug = backoffice_vacature.slug,
        existing_vacature.titel = backoffice_vacature_content.titel,
        existing_vacature.omschrijving = backoffice_vacature_content.omschrijving
        existing_vacature.save()
    except Vacature.DoesNotExist:
        Vacature(
            slug = backoffice_vacature.slug,
            titel = backoffice_vacature_content.titel,
            omschrijving = backoffice_vacature_content.omschrijving
        ).save()

def removeFromFrontOffice(backoffice_vacature):
    try:
       Vacature.objects.get(slug=backoffice_vacature.slug).delete()
    except Vacature.DoesNotExist:
        None