from django.contrib import admin
from .models import Profile
from .User import User

# Register your models here.
admin.site.register([User, Profile])

