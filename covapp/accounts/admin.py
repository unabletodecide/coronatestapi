from django.contrib import admin
from .models import CustomUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()

class CustomUserAdmin(BaseUserAdmin):
    """Define admin model for custom User model with no username field."""
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('firstname', 'lastname', 'country')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    ordering = ('email',)
    list_display = ('email', 'firstname', 'lastname', 'country', 'is_staff', 'is_superuser')
    search_fields = ('email', 'firstname', 'lastname')

admin.site.register(CustomUser, CustomUserAdmin)