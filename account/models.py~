# -*-coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class UserMessage(models.Model):
	object_id = models.CharField(max_length=100,primary_key=True,default=" ",verbose_name="mainkey")
	name = models.CharField(max_length = 20,verbose_name=u"名字")
	email = models.EmailField(verbose_name=u"邮箱")
	address = models.CharField(max_length = 30,verbose_name=u"地址")
	message = models.CharField(max_length = 300,verbose_name=u"评论")
	#message = models.Content=UEditorField(max_length = 500,verbose_name=u'内容',width=600, height=300, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000},
            # default='')

	class Meta:
		verbose_name = u"用户评论"
		verbose_name_plural = verbose_name
