from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Vacature
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'frontoffice/index.html'
    context_object_name = 'vacatures'

    def get_queryset(self):
        """Return the last five published vacatures."""
        return Vacature.objects.filter(
        ).order_by('-dateCreated')[:5]

def detail(request, slug):
    try:
        vacature = Vacature.objects.get(slug=slug)
    except Vacature.DoesNotExist:
        raise Http404("Vacature niet gevonden")
    return render(request, 'frontoffice/detail.html', {'vacature': vacature})
