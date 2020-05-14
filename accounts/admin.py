from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','last_name','first_name','email']
    list_display_links = ['username']