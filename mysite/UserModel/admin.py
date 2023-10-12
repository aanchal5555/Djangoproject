from django.contrib import admin

# Register your models here.

from UserModel.models import userauthentication

class AdminUser(admin.ModelAdmin):
    list_display=('username','password')

admin.site.register(userauthentication,AdminUser) 




