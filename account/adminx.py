#from django.contrib import admin

#Register your models here.
import xadmin
from .models import UserProfile

class UserProfileAdmin(object):
	pass
	
xadmin.site.register(UserProfile,UserProfileAdmin)
