# -*-coding:utf-8 -*-
#from django.contrib import admin

#Register your models here.
import xadmin
from .models import UserProfile,EmailVerifyRecord

class UserProfileAdmin(object):
	list_display = ['nick_name','birday','gender','address','mobile']
	search_fields = ['nick_name','birday','gender','address','mobile']
	list_filter = ['nick_name','birday','gender','address','mobile']


class EmailVerifyRecordAdmin(object):
	list_display = ['code','send_type','send_time']
	search_fields = ['code','send_type','send_time']
	list_filter = ['code','send_type','send_time']



xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)


