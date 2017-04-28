import KilnData.models as KilnModels
from KilnRestAPI.user_serializers import UserSerializer
from rest_framework import serializers

# <editor-fold desc="Super User Serializers">

class KilnUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer()
    class Meta:
        model = KilnModels.KilnUserProfile
        fields = ('url', 'temperature_display_units', 'user')

class ProgramStepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KilnModels.ProgramStep
        fields = ('url', 'program', 'seconds', 'order', 'temperature_in_c')

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    program_steps = ProgramStepSerializer(many=True)
    class Meta:
        model = KilnModels.Program
        fields = ('url', 'program_name', 'program_type', 'program_steps')


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

# </editor-fold>

class KilnLimitedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KilnModels.Kiln
        fields = ('kiln_id', 'kiln_name')

class ProgramStepLimitedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KilnModels.ProgramStep
        fields = ('program', 'seconds', 'order', 'temperature_in_c')


class ProgramLimitedSerializer(serializers.HyperlinkedModelSerializer):
    program_steps = ProgramStepLimitedSerializer(many=True)

    class Meta:
        model = KilnModels.Program
        fields = ('program_name', 'program_type', 'program_steps')
