from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user_view import UserViewSet
from .views.purchase_view import create_purchase

router = DefaultRouter()

router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('purchase/create/', create_purchase, name="create-purchase")
]
