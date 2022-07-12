from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from .models import UserAccount
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class AdminUserConfig(UserAdmin):
    fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     )}),
    )
    add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'username', 'first_name', 'last_name', 'phone', 'password1', 'password2','is_active', 'is_staff', 'is_superuser',),
      }),
    )
    list_display = ['email', 'first_name', 'last_name', 'is_staff', "phone"]
    search_fields = ('email', 'first_name', 'last_name', 'username')
    ordering = ('email', )

admin.site.register(UserAccount, AdminUserConfig)