"""Timezone URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #GET /time
    url(r'^time$', views.get_time_at_server, name='render_server_local_time'),
    #GET /35.29,-89.66/tz
    url(r'^(?P<lat_lng_str>.+)/tz$', views.get_time_at_lat_lng, name='render_target_local_time'),
    #GET /35.29,-89.66/time
    url(r'^(?P<lat_lng_str>.+)/time$', views.get_time_at_lat_lng, name='render_target_local_time'),
    url(r'^(?P<time_str>.+)/at/(?P<lat_lng_str>.+)', views.get_time_at_time_lat_lng, name='render_translated_time'),
    #GET /2016-08-25T10:40:15-07:00/at/35.29,-89.66
    url(r'^helloworld$', views.helloworld, name='helloworld'),
]
