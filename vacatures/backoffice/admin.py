from django.contrib import admin

from .models import Vacature, VacatureContent, VacatureFeatures
from django.utils import timezone
from frontoffice.actions import publishToFrontOffice, removeFromFrontOffice
from uuid import UUID
import uuid
from utils import string_to_uuid
from django.contrib import messages

def publish(modeladmin, request, queryset):
    queryset.update(datePublished = timezone.now())
    for vacature in queryset:
        publishToFrontOffice(vacature)
        
def unPublish(modeladmin, request, queryset):
    queryset.update(datePublished = None)
    for vacature in queryset:
        removeFromFrontOffice(vacature)

class VacatureFeaturesAdmin(admin.StackedInline):
    model = VacatureFeatures
    #fields = ('code',)

class VacatureContentAdmin(admin.StackedInline):
    model = VacatureContent
    #fields = ('code',)


class VacatureAdmin(admin.ModelAdmin):
    list_display = ['content_titel', 'is_published']
    actions = [publish, unPublish]
    search_fields = ['vacaturecontent__titel', 'slug']
    inlines = [VacatureContentAdmin, VacatureFeaturesAdmin]
    
    def content_titel(self, object):
        return object.content().titel
    
    def save_model(self, request, obj, form, change):
        #if 'owner' in form.changed_data:
        #messages.add_message(request, messages.SUCCESS, 'Car has been sold')
        super(VacatureAdmin, self).save_model(request, obj, form, change)
    
publish.short_description = "Toevoegen op frontoffice"
unPublish.short_description = "Verwijder op frontoffice"

admin.site.register(Vacature, VacatureAdmin)
