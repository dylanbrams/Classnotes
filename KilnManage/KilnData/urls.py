"""KilnManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from KilnData import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<kiln_name_in>.+)/add_kiln/', views.add_kiln, name='add_kiln'),
    url(r'^add_update_kiln_data', views.add_update_kiln_data, name='add_update_kiln_data'),
    url(r'^(?P<kiln_id_in>.+)/view_kiln_data/', views.view_kiln_data, name='view_kiln_data'),
    url(r'^(?P<kiln_name_in>.+)/view_kiln/', views.view_kiln, name='view_kiln'),
    url(r'^view_env_test/', views.view_env_test, name='helloworld'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^accounts/profile/$', auth_views.profile, name='profile'),
    url(r'^$', views.home, name='home'),
]
