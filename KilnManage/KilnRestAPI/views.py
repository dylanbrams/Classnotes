from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from KilnRestAPI.user_serializers import UserSerializer, GroupSerializer
from KilnData.models import KilnUserProfile, Program, ProgramStep, Kiln, KilnAdminType, jt_Kiln_Admin, jt_Kiln_Program
from KilnRestAPI.kiln_serializers import KilnUserProfileSerializer, ProgramSerializer, ProgramStepSerializer, \
    KilnSerializer, KilnAdminTypeSerializer, jt_Kiln_AdminSerializer, jt_Kiln_ProgramSerializer


class GeneralKilnView(APIView):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    pass


# <editor-fold desc="StandardCRUD">

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class KilnUserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = KilnUserProfile.objects.all()
    serializer_class = KilnUserProfileSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramStepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ProgramStep.objects.all()
    serializer_class = ProgramStepSerializer


class KilnViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Kiln.objects.all()
    serializer_class = KilnSerializer


class KilnAdminTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = KilnAdminType.objects.all()
    serializer_class = KilnAdminTypeSerializer


class jt_Kiln_AdminViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = jt_Kiln_Admin.objects.all()
    serializer_class = jt_Kiln_AdminSerializer


class jt_Kiln_ProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = jt_Kiln_Program.objects.all()
    serializer_class = jt_Kiln_ProgramSerializer

    # </editor-fold desc="StandardCRUD">
