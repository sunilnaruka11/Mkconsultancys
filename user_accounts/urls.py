from . import views
from django.urls import path
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from smtplib import SMTPException

app_name = "user_accounts"

urlpatterns = [
    path('',views.LoginView.as_view(),name='login'),
    path('accounts/register/',views.RegisterView.as_view(),name='register'),
    path('accounts/logout/',views.LogoutView.as_view(),name="logout"),
    path('accounts/password-reset/',views.PasswordResetCustomView.as_view(),name="password_reset"),
    
    path(
        'accounts/password-reset-confirm/<uidb64>/<token>',
        views.PasswordResetConfirmCustomView.as_view(
         template_name='accounts/password_reset_confirm.html'
        ),name="password_reset_confirm"
    ),
]


		
		