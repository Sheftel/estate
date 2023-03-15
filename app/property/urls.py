from django.urls import include, path

from .views import PropertyListView, PropertyDetailView

app_name = 'property'


urlpatterns = [
    path('', PropertyListView.as_view(), name='list'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='detail')
]
