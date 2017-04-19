# -*-coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
	nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default="")
	birday = models.DateField(verbose_name=u"生日",null=True,blank=True)
	gender = models.CharField(max_length=50,choices=(("male",u"男"),("female",u"女")),default="female")
	address = models.CharField(max_length=100,default="")
	mobile = models.CharField(max_length=11,null=True,blank=True)
	image = models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=100)
	class Meta:
		verbose_name = u"用户信息"
		verbose_name_plural = verbose_name
	def  __unicode__(self):
		return self.username

class EmailVerifyRecord(models.Model):
	code = models.CharField(max_length=20,verbose_name="yanzhengma")
	email = models.EmailField(max_length=50,verbose_name="email")
	send_type = models.CharField(choices=(("register","zhuce"),("forget","zhaohuimima")),max_length=10)
	send_time = models.DateTimeField(default=datetime.now)

	class Meta:
		verbose_name = "youxiangyanzhengma"
		verbose_name_plural = verbose_name



		