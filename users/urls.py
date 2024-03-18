from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.userLogin, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('change_password/', auth_view.PasswordChangeView.as_view(template_name='users/change_password.html'), name='change_password'),
    path('password_change_done/', auth_view.PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'), name='password_change_done'),
]