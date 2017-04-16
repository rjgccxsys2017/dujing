from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserMessage(models.Model):
	object_id = models.CharField(max_length=100,primary_key=True,default=" ",verbose_name="mainkey")
	name = models.CharField(max_length = 20,verbose_name="name")
	email = models.EmailField(verbose_name="email")
	address = models.CharField(max_length = 30,verbose_name="address")
	message = models.CharField(max_length = 500,verbose_name="liuyan")

	class Meta:
		verbose_name = "yonghu_message"

		