import KilnData.models as KilnModels
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class KilnUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KilnModels.KilnUserProfile
        fields = ('url','temperature_display_units','user')



# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
