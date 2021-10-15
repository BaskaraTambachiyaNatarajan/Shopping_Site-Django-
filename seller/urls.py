from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home,name='seller'),
    path('login', views.login,name='sellerlogin'),
    path('logout', views.sellerlogout,name='sellerLogout'),
    path('add', views.add,name='add'),
    path('register', views.register,name='register')
]