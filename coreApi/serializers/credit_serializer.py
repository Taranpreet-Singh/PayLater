from rest_framework import serializers
from ..models.credit_details import CreditDetailsModel

class CreditSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CreditDetailsModel
        fields = '__all__'

        