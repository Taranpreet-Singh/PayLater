from rest_framework import serializers
from ..models.user import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserModel
        fields = '__all__'

        