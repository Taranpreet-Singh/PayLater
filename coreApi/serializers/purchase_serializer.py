from rest_framework import serializers
from ..models.purchase import PurchaseModel

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PurchaseModel
        fields = '__all__'
        