"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^profile/$', views.user_profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register_patient/$', views.register_patient, name='register_patient'),
    url(r'^register_doctor/$', views.register_doctor, name='register_doctor'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),

    url(r'^create/$', views.rec_create, name='rec_create'),
    url(r'^detail/(?P<rec_id>\d+)$', views.rec_detail, name='rec_detail'),
    url(r'^list/$', views.rec_list, name='rec_list'),
    url(r'^setpatient/$', views.set_patient, name='set_patient'),
    url(r'^visit_list/$', views.visit_list, name='visit_list'),
]
