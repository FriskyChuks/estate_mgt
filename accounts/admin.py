from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'fullname', 'phone')
    list_filter = ('email', 'fullname', 'phone', 'is_active',
                   'is_staff')
    list_display = ('email', 'fullname', 'phone', 'is_active',
                    'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'fullname',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        # ('Personal')
    )
    ordering = ('email',)


admin.site.register(CustomUser, UserAdminConfig)
