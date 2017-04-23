"""dujing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
#from django.contrib import admin

from django.views.generic import TemplateView
import xadmin

from account.views import loginView,registerView,ActiveUserView,liuyan

urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
   # url(r'^message/$',message,name='message'),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url('^$',TemplateView.as_view(template_name="index.html"),name="index"),
    url('^login/$',loginView.as_view(),name="login"),
    url('^register/$',registerView.as_view(),name="register"),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="user_active"),
    url(r'^liuyan/$',liuyan,name='liuyan'),
 

]
