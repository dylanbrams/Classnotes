import KilnData.models as KilnModels
from KilnRestAPI.user_serializers import UserSerializer
from rest_framework import serializers

class KilnUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer()
    class Meta:
        model = KilnModels.KilnUserProfile
        fields = ('url','temperature_display_units','user')

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KilnModels.Program
        fields = ('url', 'program_name', 'program_type')

class ProgramStepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KilnModels.ProgramStep
        fields = ('url', 'program', 'seconds', 'temperature_in_c')

class KilnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KilnModels.Kiln
        fields = ('url', 'kiln_name')

class KilnAdminTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KilnModels.KilnAdminType
        fields = ('url', 'kilnadmintype_name')


class jt_Kiln_AdminSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = KilnModels.jt_Kiln_Admin
        fields = ('kiln', 'user', 'kilnadmintype')
        #depth = 1

class jt_Kiln_ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KilnModels.jt_Kiln_Program
        fields = ('kiln', 'user', 'program')

