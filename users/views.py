from users.models import UserModel
from users.service import UserService
from users.serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserAuthView(ObtainAuthToken):
    _SERVICE = UserService()


    def post(self, request, *args, **kwargs):
        if request.data.get("username") is None or request.data.get("password") is None:
            return Response({"message":"Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = self._SERVICE.find_by_username(request.data.get("username"))

        if user is None:
            return Response({"message":"User not found"}, status=status.HTTP_400_BAD_REQUEST)

        if user.password == request.data.get("password"):
            user.set_password(user.password)
            user.save()

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,})
        

