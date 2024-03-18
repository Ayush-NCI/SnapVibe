from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.userLogin, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('change_password/', auth_view.PasswordChangeView.as_view(template_name='users/change_password.html'), name='change_password'),
    path('password_change/done/', auth_view.PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'), name='password_change_done'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]