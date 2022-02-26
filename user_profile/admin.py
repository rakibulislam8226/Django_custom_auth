from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

admin.site.unregister(Group)


#user_profile 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ['id','username', 'email']
  list_filter = ['id','username', 'email']




