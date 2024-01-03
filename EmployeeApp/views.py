from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Import by Sunil Naruka : --- 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from django.views import View
from django.contrib import messages
from EmployeeApp.models import *  # Import Models

@method_decorator(login_required(login_url='user_accounts:login'), name='dispatch')
class EmployeeView(View):
    template_name = 'Employee/employee_list.html'
    employee_data = Employee.objects.filter(is_active=1)

    def get(self, request):
        data = {'employee_list': self.employee_data }
        return render(request, self.template_name,data)
    

@method_decorator(login_required(login_url='user_accounts:login'), name='dispatch')
class EmployeePFESIView(View):
    template_name = 'Employee/PF_ESI_list.html'
    employee_data = Employee.objects.filter(is_active=1)

    def get(self, request):
        data = {'employee_list': self.employee_data }
        return render(request, self.template_name,data)

@method_decorator(login_required(login_url='user_accounts:login'), name='dispatch')
class EmployeeBankView(View):
    template_name = 'Employee/Bank_list.html'
    employee_data = Employee.objects.filter(is_active=1)

    def get(self, request):
        data = {'employee_list': self.employee_data }
        return render(request, self.template_name,data)