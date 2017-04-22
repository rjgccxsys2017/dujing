# -*-coding:utf-8 -*-
from account.models import EmailVerifyRecord
from django.core.mail import send_mail
from dujing.settings import EMAIL_FROM

def send_register_email(email,send_type="register"):
	email_record = EmailVerifyRecord()
	code = random_str(16)
	email_record.code = code
	email_record.email = email
	email_record.send_type = send_type
	email_record.save()


	email_title = ""
	email_body = ""

	if send_type == "register":
		email_title = "dujingwangzhaixianjihuolianjie"
		email_body = "qingdainjixiamiandelianjiejihuonidezhanghao:http://127.0.0.0.1:8000/active/{0}.format(code)"
		send_status=send_email(email_title,email_body,EMAIL_FROM,[email])
		if send_status:
			pass


def random_str(randomlength=8):
	str=''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		str+=chars[random.randint(0,length)]
	return str

