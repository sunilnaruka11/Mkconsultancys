
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from smtplib import SMTPException

def send_reset_email(to_email, reset_url):
    print("email",to_email)
    print("link",reset_url)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [to_email]
    email_subject = 'Password Reset'
    email_massage = f'Click the link below to reset your password:\n\n{reset_url}'
    try:
        send_mail(email_subject, email_massage, from_email, recipient_list, fail_silently=False)
        # print("Email sent successfully.")
        return "Email sent successfully."
		
    except SMTPException as e:
	
        print(f"Email not sent. Error: {e}")
        return "Sorry !!! Email not sent successfully."