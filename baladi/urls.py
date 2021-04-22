"""baladi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api.views import *
from rest_framework import routers
from baladi.api import router
from django.contrib.auth import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/app/', include(router.urls)),
    #path('api/auth/', include('djoser.urls.authtoken')),
    #path('api-token-auth/', obtain_auth_token),
    #path('login/', login),
    #path('api-auth/',include('rest_framework.urls')),
    path('register',SignupView.as_view()),
    path('csrf_cookie', GetCSRFToken.as_view()),
    path('authenticated', CheckAuthView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('delete', DeleteAccountView.as_view()),
    path('citizen_profile',GetCitizenProfileView.as_view() ),
    path('update_citizen_profile', UpdateCitizenProfileView.as_view()),

]

