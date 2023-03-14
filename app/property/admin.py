from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Owner, Property


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'type']}),
        (_('Contacts'), {'fields': ['phone', 'email']})
    ]

    list_display = ('name', 'type', 'email', 'phone')
    list_filter = ('type',)
    search_fields = ('name', 'type', 'user.email', 'phone')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['owner', 'deal', 'price']}),
        (_('Details'), {'fields': ['type', 'category', 'area', 'floor', 'room_count', 'address', 'description']})
    ]

    list_display = ('category', 'deal', 'room_count', 'floor', 'type', 'address', 'category', 'area', 'owner')
    list_filter = ('room_count', 'floor', 'price', 'deal', 'type', 'category', 'owner')
    search_fields = ('address', 'room_count')
