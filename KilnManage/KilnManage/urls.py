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
from KilnData import views as KilnDataViews
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers
from KilnRestAPI import views as rest_API_views


router = routers.DefaultRouter()
router.register(r'kilnedits', rest_API_views.GeneralKilnView)

# Basic CRUD operations with standard REST API
router.register(r'users', rest_API_views.UserViewSet)
router.register(r'groups', rest_API_views.GroupViewSet)
router.register(r'kilnuserprofile', rest_API_views.KilnUserProfileViewSet)
router.register(r'program', rest_API_views.ProgramViewSet)
router.register(r'programstep', rest_API_views.ProgramStepViewSet)
router.register(r'kiln', rest_API_views.KilnViewSet)
router.register(r'kilnadmintype', rest_API_views.KilnAdminTypeViewSet)
router.register(r'jtkilnadmin', rest_API_views.jt_Kiln_AdminViewSet)
router.register(r'jtkilnprogram', rest_API_views.jt_Kiln_ProgramViewSet)

urlpatterns = [
    #Kilns
    url(r'^add_kiln/(?P<kiln_name_in>.+)/', KilnDataViews.add_kiln, name='add_kiln'),
    url(r'^add_update_kiln_data', KilnDataViews.add_update_kiln_data, name='add_update_kiln_data'),
    url(r'^view_kiln_data/(?P<kiln_id_in>.+)/', KilnDataViews.view_kiln_data, name='view_kiln_data'),
    url(r'^view_kiln/(?P<kiln_name_in>.+)/', KilnDataViews.view_kiln, name='view_kiln'),

    #Programs (firing programs}
    url(r'^add_program/', KilnDataViews.add_program, name='add_program'),

    #Env Test (a hello world)
    url(r'^view_env_test/', KilnDataViews.view_env_test, name='helloworld'),

    #admin / login / logout
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^api/', include(router.urls)),

    url(r'^$', KilnDataViews.home, name='home'),
    url(r'^silk', include('silk.urls', namespace='silk')),
]

