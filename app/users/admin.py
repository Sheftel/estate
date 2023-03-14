from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


from .models import Client

User = get_user_model()

admin.register(User, UserAdmin)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'type']}),
        (_('Personal Info'), {'fields': ['age', 'sex', 'partner', 'kids']}),
    ]

    list_display = ('user', 'type', 'age')
    list_filter = ('type',)
    search_fields = ('user', 'type',)




# class OwnerInline(admin.StackedInline):
#     model = Owner
#     can_delete = False
#     verbose_name_plural = 'owner'

#
# @admin.site.register(User)
# class UserAdmin(admin.ModelAdmin):
#     fieldsets = ...
#     inlines = (ClientInline, OwnerInline)
#

