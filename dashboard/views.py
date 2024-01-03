from django.shortcuts import render
from django.views import View


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='user_accounts:login'), name='dispatch')
class DashboardView(View):

    template_name = 'dashboard/pages/dashboard_home.html'

    def get(self, request):
        return render(request, self.template_name)
    
@method_decorator(login_required(login_url='user_accounts:login'), name='dispatch')
class UserProfileView(View):
  
    template_name = 'dashboard/pages/dashboard_profile.html'

    def get(self, request):
        return render(request, self.template_name)
