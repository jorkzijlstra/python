from django.contrib import admin

from .models import Vacature
from django.utils import timezone
from frontoffice.actions import publishToFrontOffice, removeFromFrontOffice

def publish(modeladmin, request, queryset):
    queryset.update(datePublished = timezone.now())
    for vacature in queryset:
        publishToFrontOffice(vacature)
        
def unPublish(modeladmin, request, queryset):
    queryset.update(datePublished = None)
    for vacature in queryset:
        removeFromFrontOffice(vacature)
    
class VacatureAdmin(admin.ModelAdmin):
    list_display = ['titel', 'slug', 'is_published']
    actions = [publish, unPublish]

publish.short_description = "Toevoegen op frontoffice"
unPublish.short_description = "Verwijder op frontoffice"

admin.site.register(Vacature, VacatureAdmin)
