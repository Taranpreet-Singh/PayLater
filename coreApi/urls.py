from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, create_purchase

router = DefaultRouter()

router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-purchase/', create_purchase, name="create-purchase")
]
