"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

'''
You should always use include() when you include other URL patterns. 
admin.site.urls is the only exception to this.
'''

'''
route is a string that contains a URL pattern. When processing a request, 
Django starts at the first pattern in urlpatterns and makes its way down the list, 
comparing the requested URL against each pattern until it finds one that matches.
'''

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('portal/', include('portal.urls')),
    path('', include('django.contrib.auth.urls')),
]
