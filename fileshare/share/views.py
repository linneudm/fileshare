from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import  reverse, reverse_lazy
from django.contrib import messages
from .models import *
from datetime import date
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


# File CRUD
class FileList(ListView):

	paginate_by = 50

	model = File
	template_name = 'file/list.html'

	def get_queryset(self):
		self.queryset = super(FileList, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(description__icontains = self.request.GET['search_box'])
		return self.queryset

class FileDetail(DetailView):
	model = File
	template_name = 'file/details.html'

class FileCreate(CreateView):
	model = File
	template_name = 'file/add.html'
	form_class = FileForm
	def form_valid(self,form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

class FileUpdate(UpdateView):
	model = File
	template_name = 'file/add.html'
	form_class = FileForm
	success_url = reverse_lazy('share:file_list')

class FileDelete(DeleteView):
	model = File
	success_url = reverse_lazy('share:file_list')

# End File