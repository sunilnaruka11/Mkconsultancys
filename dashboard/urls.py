from . import views as deshboard_views


from django.urls import path

app_name = "dashboard"

urlpatterns = [
    path('',deshboard_views.DashboardView.as_view(),name='home'),
    path('profile/',deshboard_views.UserProfileView.as_view(),name='profile'),

 
]
