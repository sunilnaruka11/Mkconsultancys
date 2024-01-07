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

# Import necessary modules for upload files
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

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



def get_user_input_from_html_form(request):
          
            """
    Retrieves user input data from the HTML form in the task application.
    Parameters:
        - request: The HTTP request object containing user input.
    Returns:
        A dictionary containing user input data.
    """
            
             # Example: Get task name from the form  
            Employeecode = request.POST.get('Employeecode')
            EmployeeName = request.POST.get('EmployeeName')
            FatherName = request.POST.get('FatherName')
            
            DOB = request.POST.get('DOB')
            DOB_instance = DOB if DOB else None
             
            MobileNo = request.POST.get('MobileNo')
            LocalAddress = request.POST.get('LocalAddress')
            PermanteAddress = request.POST.get('PermanteAddress')
            PermanteState = request.POST.get('PermanteState')

            AddharNo = request.POST.get('AddharNo')
        
            BankID = request.POST.get('BankName')
            BankName_instance = None if BankID in ('', None) else Bank.objects.get(pk=BankID)
           
            IFCECode = request.POST.get('IFCECode')
            AccountNo = request.POST.get('AccountNo')

            Designation = request.POST.get('Designation')
            Designation_instance = None if Designation in ('', None) else Dasignation.objects.get(pk=Designation)

            Category = request.POST.get('Category')
            Category_instance = None if Category in ('', None) else Emp_category.objects.get(pk=Category)

            ZoneLocation = request.POST.get('ZoneLocation')
            ZoneLocation_instance = None if ZoneLocation in ('', None) else Emp_zone_location.objects.get(pk=ZoneLocation)

            WorkLocation = request.POST.get('WorkLocation')
            WorkLocation_instance = None if WorkLocation in ('', None) else Emp_work_location.objects.get(pk=WorkLocation)
            
            PFNo = request.POST.get('PFNo')
            ESINo = request.POST.get('ESINo')
            Salary = request.POST.get('Salary')

            # StartDate = request.POST.get('StartDate')
            # StartDate_instance = StartDate if StartDate else None

            # Create and return a dictionary with user input data
            MyList = {     'Employeecode':Employeecode ,
                           'EmployeeName':EmployeeName ,
                           'FatherName':FatherName,
                           'DOB_instance':DOB_instance ,
                           'MobileNo':MobileNo ,
                           'LocalAddress':LocalAddress ,
                           'PermanteAddress':PermanteAddress ,
                           'PermanteState':PermanteState ,
                           'AddharNo':AddharNo ,
                           'BankName_instance':BankName_instance,
                           'IFCECode':IFCECode ,
                           'AccountNo':AccountNo ,
                           'AddharNo':AddharNo ,
                           'Designation_instance':Designation_instance,
                           'Category_instance':Category_instance ,
                           'ZoneLocation_instance':ZoneLocation_instance,
                           'WorkLocation_instance':WorkLocation_instance ,
                           'PFNo':PFNo ,
                           'ESINo':ESINo ,
                           'Salary':Salary 
                          } 
            # print("MyList:", MyList)
            return MyList   

@method_decorator(login_required(login_url='user_accounts:login'), name='dispatch')
class EmployeeAdd(View):
    template_name = 'Employee/employee_add.html'
    yourmasage = None

    emp_category_data = Emp_category.objects.filter(is_active=1) 
    emp_zone_data = Emp_zone_location.objects.filter(is_active=1) 
    emp_work_location_data = Emp_work_location.objects.filter(is_active=1)  
    emp_designation_data = Dasignation.objects.filter(is_active=1)
    emp_bank_data = Bank.objects.filter(is_active=1)

    data = { 
              'category_list':emp_category_data,
              'zone_location_list':emp_zone_data,  
              'work_location_list':emp_work_location_data,
              'designation_list':emp_designation_data,
              'emp_bank_list':emp_bank_data,        
           }
    
    def get(self, request):
        return render(request, self.template_name,self.data)
    
    def post(self,request,*args, **kwargs):
            
            """ The function get_user_input_from_html_form takes a request parameter, which is the 
                HTTP request object. It retrieves user input data using request.POST.get() for each
                form field """
            
            UserPostedData=get_user_input_from_html_form(request)

            # Check if a AAdhar file was uploaded
            uploaded_aadhar_file = request.FILES.get('AddharFile')
            file_aadhar_path = None

            if uploaded_aadhar_file: 
                # Generate a unique filename with timestamp
                current_time = datetime.now().strftime("%Y%m%d%H%M%S")
                filename = f'{current_time}_{uploaded_aadhar_file.name}'
                # Specify the subdirectory within MEDIA_ROOT
                subdirectory = 'aadhar_files'
                # Construct the file path with the subdirectory
                file_aadhar_path = default_storage.save(f'{subdirectory}/{filename}', ContentFile(uploaded_aadhar_file.read()))
                
            else:
                file_aadhar_path=None

            print("My AAdhar =",file_aadhar_path)
           
             # Check if a BankPassbook file was uploaded
            uploaded_passbook_file = request.FILES.get('PassbookFile')
            file_passbook_path = None
            if uploaded_passbook_file: 
                # Generate a unique filename with timestamp
                current_time = datetime.now().strftime("%Y%m%d%H%M%S")
                filename = f'{current_time}_{uploaded_passbook_file.name}'
                # Specify the subdirectory within MEDIA_ROOT
                subdirectory = 'passbook_files'
                # Construct the file path with the subdirectory
                file_passbook_path = default_storage.save(f'{subdirectory}/{filename}', ContentFile(uploaded_passbook_file.read()))
            else:
                file_passbook_path=None
           
          # Create an instance of the model
            
            Employee_instance = Employee(
                 
            emp_code = UserPostedData['Employeecode'],     
            emp_name = UserPostedData['EmployeeName'], 
            emp_father_name = UserPostedData['FatherName'],
            emp_dob = UserPostedData['DOB_instance'],
            emp_mobile_no = UserPostedData['MobileNo'],
         
            emp_permante_address = UserPostedData['PermanteAddress'],
            emp_permante_state = UserPostedData['PermanteState'],
            emp_local_address = UserPostedData['LocalAddress'],
            emp_addhar_no = UserPostedData['AddharNo'],
            aadhar_file = file_aadhar_path,

            emp_bank_id = UserPostedData['BankName_instance'],
            emp_bank_ifsc_code = UserPostedData['IFCECode'],
            emp_bank_ac_no = UserPostedData['AccountNo'],
            bank_passbook_file = file_passbook_path,
           
            emp_designation_id = UserPostedData['Designation_instance'],
            emp_category_id = UserPostedData['Category_instance'],
            emp_zone_loation_id = UserPostedData['ZoneLocation_instance'],
            emp_work_location_id = UserPostedData['WorkLocation_instance'],
           
            emp_pf_no = UserPostedData['PFNo'],
            emp_esi_no = UserPostedData['ESINo'],
            emp_salary_ctc = UserPostedData['Salary']

            )

        # Save the instance to the database
            Employee_instance.save()
            self.yourmasage = " Employee created successfully " 
            messages.success(request,self.yourmasage)
            return render(request, self.template_name,self.data)

@method_decorator(login_required(login_url='user_accounts:login'), name='dispatch')
class EmployeeEdit(View):
     
    template_name = 'Employee/employee_edit.html'
    yourmasage = None
    
    emp_category_data = Emp_category.objects.filter(is_active=1) 
    emp_zone_data = Emp_zone_location.objects.filter(is_active=1) 
    emp_work_location_data = Emp_work_location.objects.filter(is_active=1)  
    emp_designation_data = Dasignation.objects.filter(is_active=1)
    emp_bank_data = Bank.objects.filter(is_active=1)

    def get(self, request,pk):
        try:
            employee_details_data = get_object_or_404(Employee, pk=pk)
           
            data = {   'category_list':self.emp_category_data,
                       'zone_location_list':self.emp_zone_data,  
                       'work_location_list':self.emp_work_location_data,
                       'designation_list':self.emp_designation_data,
                       'emp_bank_list':self.emp_bank_data,
                       'employee_details': employee_details_data
                   }          
        except Employee.DoesNotExist:
            self.yourmasage = "Your record not found."
            messages.success(request, self.yourmasage)
            return render(request, self.template_name)    
        return render(request, self.template_name, data)
    
    def post(self,request,*args, **kwargs,):
            
            url = reverse_lazy('Employee:employee')
            pk = kwargs.get('pk')

            Employee_instance  = get_object_or_404(Employee, pk=pk)            
            UserPostedData=get_user_input_from_html_form(request)

             # Check if a AAdhar file was uploaded
            uploaded_aadhar_file = request.FILES.get('AddharFile')
            file_aadhar_path = None

            if uploaded_aadhar_file: 
                # Generate a unique filename with timestamp
                current_time = datetime.now().strftime("%Y%m%d%H%M%S")
                filename = f'{current_time}_{uploaded_aadhar_file.name}'
                # Specify the subdirectory within MEDIA_ROOT
                subdirectory = 'aadhar_files'
                # Construct the file path with the subdirectory
                file_aadhar_path = default_storage.save(f'{subdirectory}/{filename}', ContentFile(uploaded_aadhar_file.read()))
                
            else:
                file_aadhar_path=Employee_instance.aadhar_file.path if Employee_instance.aadhar_file else None

            print("My AAdhar =",file_aadhar_path)
           
             # Check if a BankPassbook file was uploaded
            uploaded_passbook_file = request.FILES.get('PassbookFile')
            file_passbook_path = None
            if uploaded_passbook_file: 
                # Generate a unique filename with timestamp
                current_time = datetime.now().strftime("%Y%m%d%H%M%S")
                filename = f'{current_time}_{uploaded_passbook_file.name}'
                # Specify the subdirectory within MEDIA_ROOT
                subdirectory = 'passbook_files'
                # Construct the file path with the subdirectory
                file_passbook_path = default_storage.save(f'{subdirectory}/{filename}', ContentFile(uploaded_passbook_file.read()))
            else:
                file_passbook_path=Employee_instance.bank_passbook_file.path if Employee_instance.bank_passbook_file else None
           

            Employee_instance.emp_code = UserPostedData['Employeecode']     
            Employee_instance.emp_name = UserPostedData['EmployeeName'] 
            Employee_instance.emp_father_name = UserPostedData['FatherName']
            Employee_instance.emp_dob = UserPostedData['DOB_instance']
            Employee_instance.emp_mobile_no = UserPostedData['MobileNo']
            Employee_instance.emp_permante_address = UserPostedData['PermanteAddress']
            Employee_instance.emp_permante_state = UserPostedData['PermanteState']
            Employee_instance.emp_local_address = UserPostedData['LocalAddress']
            Employee_instance.emp_addhar_no = UserPostedData['AddharNo']

            Employee_instance.aadhar_file = file_aadhar_path
            
            Employee_instance.emp_bank_id = UserPostedData['BankName_instance']
            Employee_instance.emp_bank_ifsc_code = UserPostedData['IFCECode']
            Employee_instance.emp_bank_ac_no = UserPostedData['AccountNo']
            
            Employee_instance.bank_passbook_file = file_passbook_path
           
            Employee_instance.emp_designation_id = UserPostedData['Designation_instance']
            Employee_instance.emp_category_id = UserPostedData['Category_instance']
            Employee_instance.emp_zone_loation_id = UserPostedData['ZoneLocation_instance']
            Employee_instance.emp_work_location_id = UserPostedData['WorkLocation_instance']
           
            Employee_instance.emp_pf_no = UserPostedData['PFNo']
            Employee_instance.emp_esi_no = UserPostedData['ESINo']
            Employee_instance.emp_salary_ctc = UserPostedData['Salary']        

            # # Save the instance to the database
            Employee_instance.save()
            self.yourmasage = " Employee updated successfully " 
            messages.success(request,self.yourmasage)
            return redirect(url)
