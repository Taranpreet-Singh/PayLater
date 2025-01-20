from ..serializers.user_serializer import UserSerializer
from ..models import UserModel
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer