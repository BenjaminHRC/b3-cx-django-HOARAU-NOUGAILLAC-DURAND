from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    # path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.logout_view, name='logout')
]