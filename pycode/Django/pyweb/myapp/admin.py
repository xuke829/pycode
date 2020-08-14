from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'mid', 'name', 'sign', 'level')
    list_display_links = ('mid', 'name')


admin.site.register(User, UserAdmin)
