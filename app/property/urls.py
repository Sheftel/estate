from django.urls import include, path

from .views import PropertyListView, PropertyDetailView, FavouriteListView, AddFavouriteView

app_name = 'property'


urlpatterns = [
    path('', PropertyListView.as_view(), name='list'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='detail'),
    path('<int:pk>/to_favourite', AddFavouriteView.as_view(), name='add_favourite'),
    path('favourites/', FavouriteListView.as_view(), name='favourites')
]
