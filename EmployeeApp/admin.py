from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Emp_category)
class EmpCategoryAdmin(admin.ModelAdmin):
	list_display =  Emp_category.DisplayFields
	list_filter = Emp_category.FilterFields

@admin.register(Dasignation)
class EmpDasignationAdmin(admin.ModelAdmin):
	list_display =  Dasignation.DisplayFields
	list_filter = Dasignation.FilterFields

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
	list_display =  Bank.DisplayFields
	list_filter = Bank.FilterFields

@admin.register(Emp_zone_location)
class EmpZoneLocationAdmin(admin.ModelAdmin):
	list_display = Emp_zone_location.DisplayFields
	list_filter = Emp_zone_location.FilterFields

@admin.register(Emp_work_location)
class EmpWorkLocationAdmin(admin.ModelAdmin):
	list_display =  Emp_work_location.DisplayFields
	list_filter = Emp_work_location.FilterFields
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display =  Employee.DisplayFields
	list_filter = Employee.FilterFields