from rest_framework import serializers
from owners.models import OwnerModel

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerModel
        fields = ("__all__")
        
