from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from ..models import Property

__all__ = [
    'PropertyListView',
    'PropertyDetailView'
]


class PropertyListView(ListView):
    model = Property

    def get(self, request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_authenticated:
            return redirect('users:signin')
        elif not hasattr(current_user, 'client'):
            return redirect('users:questions')
        return super().get(self, request, *args, **kwargs)


class PropertyDetailView(DetailView):
    model = Property
