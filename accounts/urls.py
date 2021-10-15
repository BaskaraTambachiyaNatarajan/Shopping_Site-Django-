from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name='Login'),
    path('register', views.register,name='Register'),
    path('logout', views.logout,name='Logout'),
    path('myaccount', views.myaccount,name='MyAccount'),
    path('update_session', views.updatesession,name='updatesession')
]