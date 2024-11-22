from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, View
from .models import PR, StatusPR
from .forms import PRForm, StatusPRForm
class ListPR(ListView):
    template_name = 'crud_pr/tables.html'
    model = PR
    context_object_name = "list_pr"

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
