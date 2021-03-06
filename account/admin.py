from django.contrib import admin

# Register your models here.
from .models import UserProfile

class UserprofileAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'user', 'bio', 'profile_pic')
    list_display_links = ('id', 'user')

admin.site.register(UserProfile, UserprofileAdmin)