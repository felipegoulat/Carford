from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from cars.models import CarModel
from cars.serializers import CarSerializer, CarRetrieveSerializer


class CarViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CarRetrieveSerializer
        return super().retrieve(request, *args, **kwargs)

    
    def list(self, request, *args, **kwargs):
        self.serializer_class = CarRetrieveSerializer
        return super().list(request, *args, **kwargs)