from django.shortcuts import render
from django.views import View

class DashboardView(View):
  
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self,request):

        name = request.POST.get('name')
        print("My name ====",name)
        return render(request, self.template_name)
    

