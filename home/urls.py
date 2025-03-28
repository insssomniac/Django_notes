from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutFormView.as_view(), name='logout'),
]
