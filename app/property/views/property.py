from django.views.generic import ListView, DetailView

from ..models import Property

__all__ = [
    'PropertyListView',
    'PropertyDetailView'
]


class PropertyListView(ListView):
    model = Property


class PropertyDetailView(DetailView):
    model = Property
