from django.db import models
# Create your models here. 

class Bank(models.Model):
    bank_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    DisplayFields = ['id','bank_name','description','is_active','created_at','updated_at']
    FilterFields =  ['created_at','updated_at','is_active']

    def __str__(self):
        return self.bank_name

class Dasignation(models.Model):
    dasignation_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    DisplayFields = ['id','dasignation_name','description','is_active','created_at','updated_at']
    FilterFields =  ['created_at','updated_at','is_active']

    def __str__(self):
        return self.dasignation_name

class Emp_category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    DisplayFields = ['id','name','description','is_active','created_at','updated_at']
    FilterFields =  ['created_at','updated_at','is_active']

    def __str__(self):
        return self.name

class Emp_zone_location(models.Model):
    zone_location_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    DisplayFields = ['id','zone_location_name','description','is_active','created_at','updated_at']
    FilterFields =  ['created_at','updated_at','is_active']

    def __str__(self):
        return self.zone_location_name

class Emp_work_location(models.Model):
    work_location_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    DisplayFields = ['id','work_location_name','description','is_active','created_at','updated_at']
    FilterFields =  ['created_at','updated_at','is_active']

    def __str__(self):
        return self.work_location_name

class Employee(models.Model):
    
    emp_code = models.CharField(max_length=50)
    emp_name = models.CharField(max_length=50)
    emp_father_name = models.CharField(max_length=100,blank=True)
    emp_dob = models.DateField(max_length=20,blank=True,null=True)
    emp_mobile_no = models.CharField(max_length=20,blank=True)
    
    emp_email = models.EmailField(max_length=200,null=True,blank=True)

    emp_permante_address = models.TextField(max_length=300,blank=True)
    emp_permante_state = models.CharField(max_length=100,blank=True)
    emp_local_address = models.TextField(max_length=300,blank=True)
    emp_addhar_no = models.CharField(max_length=15,blank=True)
    aadhar_file = models.FileField(upload_to='aadhar_card/',null=True, blank=True , default=None)

    emp_bank_id = models.ForeignKey(Bank, null=True,blank=True, on_delete=models.SET_NULL)  #
    emp_bank_ifsc_code = models.CharField(max_length=10,null=True,blank=True)
    emp_bank_ac_no = models.CharField(max_length=50,null=True,blank=True)
    bank_passbook_file = models.FileField(upload_to='bank_passbook/',null=True, blank=True , default=None)
    
    emp_designation_id = models.ForeignKey(Dasignation,blank=True, null=True, on_delete=models.SET_NULL)
    emp_category_id = models.ForeignKey(Emp_category, null=True,blank=True, on_delete=models.SET_NULL)
    emp_zone_loation_id = models.ForeignKey(Emp_zone_location, null=True,blank=True, on_delete=models.SET_NULL)
    emp_work_location_id = models.ForeignKey(Emp_work_location, null=True,blank=True, on_delete=models.SET_NULL)

    emp_pf_no = models.CharField(max_length=100,blank=True)
    emp_esi_no = models.CharField(max_length=100,blank=True)
    emp_salary_ctc = models.CharField(max_length=100,blank=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    DisplayFields = ['id','emp_code','emp_name','emp_father_name','emp_bank_id','is_active','created_at','updated_at']
    FilterFields =  ['created_at','updated_at','is_active']

    def __str__(self):
        return f'{self.emp_name} {self.emp_father_name}'
