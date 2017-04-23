# -*-coding:utf-8 -*-
#from django.contrib import admin

#Register your models here.
import xadmin
from .models import UserProfile,EmailVerifyRecord
from xadmin import views

class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True

class GlobalSettings(object):
	site_title = u"独景后台管理系统"
	site_footer = u"独景网"
	menu_style = "accordion"


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
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)



