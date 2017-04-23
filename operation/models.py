# -*-coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from DjangoUeditor.models import UEditorField
from django.db import models

from account.models import UserProfile

# Create your models here.
class Comments(models.Model):
	user = models.ForeignKey(UserProfile,verbose_name = u"用户")
	comments = models.CharField(max_length=200,verbose_name=u"评论")
	add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"用户评论"
		verbose_name_plural = verbose_name



class UserFavorite(models.Model):
	user = models.ForeignKey(UserProfile,verbose_name=u"用户")
	fav_id = models.IntegerField(default=0,verbose_name=u"数据ID")
	fav_type = models.IntegerField(choices=((1,u"用户"),(2,u"文章")),default=1,verbose_name=u"收藏类型")
	add_time = models.DateTimeField(default=datetime.now,verbose_name=u"收藏时间")

	class Meta:
		verbose_name = u"用户收藏"
		verbose_name_plural = verbose_name


class UserMessage(models.Model):
	user = models.IntegerField(default=0,verbose_name=u"接收用户")
	message = UEditorField(width=600, height=300,imagePath="message/ueditor/", filePath="message/ueditor/",verbose_name=u"消息内容",default='')
	has_read = models.BooleanField(default=False,verbose_name=u"是否已读")
	add_time = models.DateTimeField(default=datetime.now,verbose_name=u"收藏时间")
	class Meta:
		verbose_name = u"用户消息"
		verbose_name_plural = verbose_name
