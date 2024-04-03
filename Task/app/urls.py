from django.urls import path
from app import views

urlpatterns=[
    path('',views.Login,name="Login"),
    path('register',views.Register,name='register')
]