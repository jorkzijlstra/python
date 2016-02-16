from django.utils import timezone
from frontoffice.actions import publishToFrontOffice, removeFromFrontOffice
from .models import Vacature, VacatureContent, VacatureFeatures

def publish(modeladmin, request, queryset):
    queryset.update(datePublished = timezone.now())
    for vacature in queryset:
        publishToFrontOffice(vacature)
        
def unPublish(modeladmin, request, queryset):
    queryset.update(datePublished = None)
    for vacature in queryset:
        removeFromFrontOffice(vacature)