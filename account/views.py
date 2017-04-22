from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth import authenticate,login
# Create your views here.
# 
from django.contrib.auth.backends import ModelBackend
from django.views.generic.base import View
from .models import UserProfile
from .forms import loginForm,registerForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
#
class CustomBackend(ModelBackend):
	def authenticate(self,username=None,password=None,**kwargs):
		try:
			user=UserProfile.objects.get(username=username)
			if user.check_password(password):
				return user
		except Exception as e:
			return None


class registerView(View):
	def get(self,request):
		register_form = registerForm()
		return render(request,"register.html",{'register_form':register_form})
	def post(self,request):
		register_form = registerForm(request.POST)
		if register_form.is_valid():
			user_name = request.POST.get("email","")
			pass_word = request.POST.get("password","")
			user_profile = UserProfile()
			user_profile.username = user_name
			user_profile.email = user_name
			user_profile.password = make_password(pass_word)
			user_profile.save()
			
			send_register_email(user_name,"register")
			return render(request,"login.html")
		else:
			return render(request,"register.html")



class loginView(View):
	def get(self,request):
		return render(request,"login.html",{})
	def post(self,request):
		login_form = loginForm(request.POST)
		if login_form.is_valid():
			user_name = request.POST.get("username","")
			pass_word = request.POST.get("password","")
			user = authenticate(username=user_name,password=pass_word)
			if user is not None:
				login(request,user)
				return render(request,"index.html")
			else:
				return render(request,"login.html",{"msg":"error log in !"})

		else:
			return render(request,"login.html",{"login_form":login_form})


def user_login(request):


	if request.method == "POST":
		user_name = request.POST.get("username","")
		pass_word = request.POST.get("password","")
		user = authenticate(username=user_name,password=pass_word)
		if user is not None:
			login(request,user)
			return render(request,"index.html")

		else:
			return render(request,"login.html",{"msg":"error log in !"})


	elif request.method == "GET":
		return render(request,"login.html",{})
