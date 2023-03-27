from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from ..models import Property

__all__ = [
    'PropertyListView',
    'PropertyDetailView',
    'FavouriteListView',
    'AddFavouriteView'
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


class FavouriteListView(ListView):
    template_name = 'property_list'
    queryset = Property.objects.all()

    def get_queryset(self):
        return self.queryset.filter(client__id=self.request.user.id)


class AddFavouriteView(View):
    def post(self, request, *args, **kwargs):
        client = self.request.user.client
        client.favourites.add(Property.objects.get(pk=self.kwargs.get('pk')))
        return HttpResponse("Property %s added to favourites." % self.kwargs.get('pk'))
