from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from cbvapp.models import company
from django.urls import reverse_lazy

# Create your views here.
# class viewname(View):
#     def get(self,request):
#         return HttpResponse('<h1>This is class based view</h1>')

class indexview(TemplateView):
    template_name = 'index.html'


class companylist(ListView):
    context_object_name = 'mycompany'
    model = company

class companydetails(DetailView):
    context_object_name = 'company_details'
    model = company

class companyCreate(CreateView):
    fields=['c_name','ceo','origin']
    model = company

class companyupdate(UpdateView):
    model=company
    fields= ['c_name','ceo']

class companydelete(DeleteView):
    model = company
    success_url = reverse_lazy('list')


