from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, View
from .models import PR, StatusPR
from .forms import PRForm, StatusPRForm
from django.utils.timezone import now

class ListPR(ListView):
    template_name = 'crud_pr/tables.html'
    model = PR
    context_object_name = "list_pr"

    def get_context_data(self, **kwargs):
        # Memanggil context default dari superclass
        context = super().get_context_data(**kwargs)
        for item in context['list_pr']:
            if item.tgl_pr:
                # Menghitung durasi dalam hari
                item.durasi = (now().date() - item.tgl_pr).days
                # Menentukan apakah expired
                item.expired = item.durasi > 30
            else:
                # Set nilai default jika tgl_pr tidak ada
                item.durasi = None
                item.expired = False
        return context
        

class RegisterPR(CreateView):
    template_name = 'crud_pr/register.html'
    model = PR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    form_class = PRForm
    success_url = '/'

class UpdatePR(UpdateView):
    template_name = 'crud_pr/register.html'
    model = PR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    form_class = PRForm
    success_url = '/'

class DeletePR(DeleteView):
    #template_name = 'register.html'
    model = PR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    #form_class = PRForm
    success_url = '/'

#Class untuk Status    

class ListStatusPR(ListView):
    template_name = 'crud_status_pr/tables.html'
    model = StatusPR
    context_object_name = "list_status_pr"

class RegisterStatusPR(CreateView):
    template_name = 'crud_status_pr/register.html'
    model = StatusPR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    form_class = StatusPRForm
    success_url = reverse_lazy('list_status_pr')

class UpdateStatusPR(UpdateView):
    template_name = 'crud_status_pr/register.html'
    model = StatusPR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    form_class = StatusPRForm
    success_url = reverse_lazy('list_status_pr')

class DeleteStatusPR(DeleteView):
    #template_name = 'register.html'
    #template_name = 'crud_status_pr/register.html'
    model = StatusPR
    #fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'status', 'delete']
    #form_class = PRForm
    success_url = reverse_lazy('list_status_pr')
