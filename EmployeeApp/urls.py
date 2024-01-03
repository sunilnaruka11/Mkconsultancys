
from EmployeeApp import views as Employee_views
from django.urls import path

app_name = "Employee"

urlpatterns = [
    path('list/',Employee_views.EmployeeView.as_view(),name='employee'),
    path('PF_ESI_list/',Employee_views.EmployeePFESIView.as_view(),name='pf_esi'),
    path('Bank_list/',Employee_views.EmployeeBankView.as_view(),name='emp_banks'),
    # path('add/',Employee_views.EmployeeAdd.as_view(),name='employee_add'),
    # path('edit/<int:pk>',Employee_views.EmployeeEdit.as_view(),name='employee_edit'),
    # path('update/<int:pk>',Employee_views.EmployeeEdit.as_view(),name='employee_updates'),
]
		
		