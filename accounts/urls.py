from django.urls import path
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts.views import login, register, logout
from django.contrib.auth.views import PasswordResetView
from django.conf.urls import url


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/',  logout, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',  auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete')
    
]