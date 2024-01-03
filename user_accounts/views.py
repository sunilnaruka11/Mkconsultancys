
from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.views import View
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from django.contrib.auth.tokens import default_token_generator

# Encode the user ID
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str

# at the top of your views.py file
from .utils import send_reset_email

class RegisterView(View):
    # form = RegisterForm
    template_name = 'accounts_user/register.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        url = reverse_lazy('accounts:login')

        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            # Create a new User instance
            new_user = User(username=username,email=email,password=make_password(password))

            # Save the new user to the database
            new_user.save()
            messages.success(request, 'Successfully Registered')
            return redirect(url)
        
        return render(request, self.template_name)


class LoginView(View):
    template_name = 'accounts_user/login.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
     
        url = reverse_lazy('user_accounts:login')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user:
                dashboard_url = reverse_lazy('dashboard:home')
                login(request, authenticated_user)
                request.session['username'] = request.user.username
                return redirect(dashboard_url)
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect(url)
        return redirect(url)


class LogoutView(View):

    def post(self, request):
        url = reverse_lazy('user_accounts:login')
        messages.success(request, 'Logged out successfully')
        logout(request)
        return redirect(url)


class PasswordResetCustomView(View):
    template_name = 'accounts_user/password_reset.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        url = reverse_lazy('accounts:password_reset')

        if request.method == 'POST':
            user_email = request.POST.get('email')

            try:
                user = User.objects.get(email=user_email)
            except User.DoesNotExist:
                messages.error(request, 'Invalid email')
                return redirect(url)

            if user:
                # Generate a password reset token
                token = default_token_generator.make_token(user)
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                
                # Construct the reset password URL
                reset_url = request.build_absolute_uri(reverse_lazy('accounts:password_reset_confirm', args=[uidb64, token]))

                # Now you can send the reset email
                send_reset_email(user_email, reset_url)

                messages.success(request, "We've emailed you instructions for setting your password")
                return redirect(url)
            
        return render(request, 'your_template.html')  # Return an appropriate response or render a template
    

class PasswordResetConfirmCustomView(View):  # noqa
    template_name = "accounts_user/password_reset_confirm.html"
    success_url = reverse_lazy('accounts:login')
    
    def decode_and_convert_to_int(self,uidb64):
         # Add padding to the base64-encoded string if needed
        uidb64_padded = uidb64 + '=' * (-len(uidb64) % 4)
        bytes_value = urlsafe_b64decode(force_str(uidb64_padded))
        string_value = bytes_value.decode('utf-8')
        numeric_value = int(string_value)
        return numeric_value
        
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        return render(request, self.template_name, {'uidb64': uidb64, 'token': token})
    
    # form_class = SetPasswordCustomForm
    def post(self,request,*args, **kwargs):
            
        uidb64 = request.POST.get('uidb64')
        token = request.POST.get('token')
        new_password = request.POST.get('new_password1')

        user_id = self.decode_and_convert_to_int(uidb64)
        # Retrieve the user object using the user model
        User = get_user_model()
        try:   
            user = User.objects.get(pk=user_id)
        except (TypeError, ValueError, OverflowError,User.DoesNotExist):
            messages.error(request, "Invalid reset link.")
            return redirect(self.success_url)

        # Set the password for the user
        user.set_password(new_password)
        user.save()

        messages.success(request, "Your password has been set. You may go ahead and login.")
        return redirect(self.success_url)


