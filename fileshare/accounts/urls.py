from django.conf.urls import url
from django.contrib.auth import views
from django.contrib.auth import urls
from .views import register

urlpatterns = [
	url(r'^register/$', register, name='register'),
    # Login
    url(r'^login/$', views.login, {'template_name': 'accounts/login.html'}, name='login'), 
    url(r'^logout/$', views.logout_then_login, {'login_url': 'core:index'}, name='logout'),
]