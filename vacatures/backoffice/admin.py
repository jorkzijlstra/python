from django.contrib import admin

from .models import Vacature

#class VacatureContentAdmin(admin.StackedInline):
#    model = VacatureContent
#    fields = ['titel', 'omschrijving']


class VacatureAdmin(admin.ModelAdmin):
    list_display = ['titel', 'slug']
    #inlines = [VacatureContentAdmin]

    #def titel(self, obj):
    #    return '%s'%(obj.VacatureContent.titel)

# Register your models here.
admin.site.register(Vacature, VacatureAdmin)
#admin.site.register(VacatureContent)