from django.contrib import admin
from user.models import UserModel,Follows

# Register your models here.
admin.site.register(UserModel)
admin.site.register(Follows)