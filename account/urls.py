from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login/', views.my_login, name="my_login"),
]
