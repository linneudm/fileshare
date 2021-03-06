from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings
# Create your views here.


def register(request):
	template_name = 'accounts/register.html'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(
				username=user.username, password=form.cleaned_data['password1'])
			login(request, user)
			return redirect('core:index')
	else:
		form = UserCreationForm()
	context = {
		'form': form
	}
	return render(request, template_name, context)