from django.shortcuts import render

from .models import Vacature, VacatureContent
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'frontoffice/index.html'
    context_object_name = 'vacatures'

    def get_queryset(self):
        """Return the last five published vacatures."""
        return Vacature.objects.filter(
        ).order_by('-dateCreated')[:5]