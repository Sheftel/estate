from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


from .models import Client

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_field = ('name', 'email')
    ordering = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'type']}),
        (_('Personal Info'), {'fields': ['age', 'sex', 'partner', 'kids']}),
    ]

    list_display = ('user', 'type', 'age')
    list_filter = ('type',)
    search_fields = ('user', 'type',)
