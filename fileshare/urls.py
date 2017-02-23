"""fileshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#Import URL's
from fileshare.core import urls as core_urls 
from fileshare.share import urls as share_urls
from fileshare.accounts import urls as accounts_urls
urlpatterns = [
    url(r'^', include(core_urls, namespace='core')),
    url(r'^share/', include(share_urls, namespace='share')),
    url(r'^accounts/', include(accounts_urls, namespace='accounts')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)