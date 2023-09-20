from django.contrib import admin
from .models import User,UserProfiles
# Register your models here.
class UserDisplay(admin.ModelAdmin):
    list_display = ('email','password','last_name','first_name')

admin.site.register(User, UserDisplay)

class UserDisplay(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(UserProfiles, UserDisplay)