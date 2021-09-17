from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path as url
from django.contrib.auth import views as auth_views
from twiliomsg.views import twiliomail

urlpatterns = [
    url(r'^twilio/$', twiliomail.as_view())]
    