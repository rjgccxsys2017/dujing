# -*-coding:utf-8 -*-
from django import forms


class loginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True,min_length = 5 )