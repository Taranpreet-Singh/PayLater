from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers.user_serializer import UserSerializer
from .models import PurchaseModel, UserModel, CreditDetailsModel
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.db.models import F

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def create_purchase(request):
    user_id = request.data.get('user_id')
    ammount = request.data.get('ammount')

    if not user_id or not ammount:
        return Response({"error": "user_id, ammount, are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    user = get_object_or_404(UserModel, id=user_id)
    user_credit = get_object_or_404(CreditDetailsModel, user_id=user)

    if int(ammount) > user_credit.credit_limit:
        return Response({"error": "Purchase amount exceeds user's available credit."}, status=status.HTTP_400_BAD_REQUEST)

    purchase = PurchaseModel.objects.create(
        user_id=user,
        ammount=ammount,
    )

    CreditDetailsModel.objects.filter(user_id=user).update(credit_limit=F('credit_limit') - int(ammount))

    return Response({
        "message": "Purchase created successfully.",
        "purchase_id": purchase.purchase_id,
        "user_id": purchase.user_id.id,
        "ammount": purchase.ammount,
        "created_on": purchase.created_on,
    }, status=status.HTTP_201_CREATED)
