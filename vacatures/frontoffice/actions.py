from django.contrib import admin

from .models import Vacature

# Register your models here.
def publishToFrontOffice(backoffice_vacature):
    try:
        existing_vacature = Vacature.objects.get(slug=backoffice_vacature.slug)
        existing_vacature.slug = backoffice_vacature.slug,
        existing_vacature.titel = backoffice_vacature.titel,
        existing_vacature.omschrijving = backoffice_vacature.omschrijving
        existing_vacature.save()
    except Vacature.DoesNotExist:
        Vacature(
            slug = backoffice_vacature.slug,
            titel = backoffice_vacature.titel,
            omschrijving = backoffice_vacature.omschrijving
        ).save()

def removeFromFrontOffice(backoffice_vacature):
    try:
       Vacature.objects.get(slug=backoffice_vacature.slug).delete()
    except Vacature.DoesNotExist:
        None