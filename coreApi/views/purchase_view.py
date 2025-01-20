from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import PurchaseModel, UserModel, CreditDetailsModel, EmiModel
from django.shortcuts import get_object_or_404
from django.db.models import F

@api_view(['POST'])
def create_purchase(request):
    user_id = request.data.get('user_id')
    ammount = request.data.get('ammount')
    months = request.data.get('months', 0)
    if int(months) > 0:
        ammount = int(ammount)/int(months)

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

    if int(months) > 0:
        EmiModel.objects.create(
            user_id=user,
            purchase_id = purchase,
            duration = months-1,
        )

    CreditDetailsModel.objects.filter(user_id=user).update(credit_limit=F('credit_limit') - int(ammount))
    
    return Response({
        "message": "Purchase created successfully.",
        "purchase_id": purchase.purchase_id,
        "user_id": purchase.user_id.id,
        "ammount": purchase.ammount,
        "created_on": purchase.created_on,
    }, status=status.HTTP_201_CREATED)
