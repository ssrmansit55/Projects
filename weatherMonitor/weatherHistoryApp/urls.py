from django.conf.urls import url, include
from django.contrib import auth
from . import views

urlpatterns = [
	url(r'^$', views.mainPanel, name='main_Panel'),]