from django.conf.urls import url
#from . import views
from .views import *

urlpatterns = [
	# File
	url(r'^file/list/$', FileList.as_view(), name='file_list'),
	url(r'^file/add/$', FileCreate.as_view(), name='file_add'),
	url(r'^file/details/(?P<pk>[0-9]+)/$', FileDetail.as_view(), name='file_details'),
	url(r'^file/(?P<pk>[0-9]+)/delete/$', FileDelete.as_view(), name='file_delete'),
]