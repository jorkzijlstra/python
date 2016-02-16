from uuid import UUID
import uuid

from django.contrib import admin
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils import timezone
from frontoffice.actions import publishToFrontOffice, removeFromFrontOffice
from backoffice.common.utils import string_to_uuid
from .models import Vacature, VacatureContent, VacatureFeatures, UserWithOrganisation, Organisation
from .actions import publish, unPublish

class VacatureFeaturesAdmin(admin.StackedInline):
    model = VacatureFeatures

class VacatureContentAdmin(admin.StackedInline):
    model = VacatureContent

class VacatureAdmin(admin.ModelAdmin):
    list_display = ['content_titel', 'is_published']
    actions = [publish, unPublish]
    search_fields = ['vacaturecontent__titel', 'slug']
    inlines = [VacatureContentAdmin, VacatureFeaturesAdmin]
    
    def content_titel(self, object):
        return object.content().titel
    
publish.short_description = "Toevoegen op frontoffice"
unPublish.short_description = "Verwijder op frontoffice"

class OrganisationUserInline(admin.StackedInline):
    model = UserWithOrganisation

class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    inlines = (OrganisationUserInline, )

class OrganisationAdmin(admin.ModelAdmin):
    model = Organisation

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Vacature, VacatureAdmin)
admin.site.register(Organisation, OrganisationAdmin)

