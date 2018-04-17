

from django.urls import path
from django.conf.urls import url

from accounts import views

urlpatterns = [
    path(r'login/',views.login_page),
    path(r'register', views.register_page),
    path(r'/',views.logout),
   #url(r'^home',views.logout),
]  