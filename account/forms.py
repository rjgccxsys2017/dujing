# -*-coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


class loginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True,min_length = 5 )

class registerForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True,min_length = 5 )
	captcha = CaptchaField()