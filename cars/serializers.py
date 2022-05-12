from rest_framework import serializers
from cars.models import CarModel
from owners.serializers import OwnerSerializer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ("__all__")

    def save(self, **kwargs):
        owner = self.validated_data.get("owner")

        cars_count = CarModel.objects.filter(owner=owner.id).count()

        if cars_count >= 3:
            raise serializers.ValidationError("Attention, this owner already owns 3 cars!")

        owner.sales_opportunity = False
        owner.save()

        return super().save(**kwargs)


class CarRetrieveSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    
    class Meta:
        model = CarModel
        fields = ("__all__")