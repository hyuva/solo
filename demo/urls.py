from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('remark', views.remark, name='remark'),
    path('developer', views.developer, name='developer'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('pro', views.pro, name='pro'),
]