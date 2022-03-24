"""signformuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.signnewuser,name="signnewuser"),                                                 #'register/'
    path('',views.loginuser,name="loginuser"),
    path('Welcome/',views.Welcomepage,name="Welcomepage"),
    path('Logout/',views.logoutpage,name="logoutpage"),
    path('page1/',views.home,name="home"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminsignup/',views.adminsignup,name="adminsignup"),
    path('adminwelcome/',views.adminwelcome,name="adminwelcome")
    # path('Logout',views),
    #  path('', views.home)
]
urlpatterns += staticfiles_urlpatterns()
