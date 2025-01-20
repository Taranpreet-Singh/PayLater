from django.db import models
from .user import UserModel
from .purchase import PurchaseModel

class EmiModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False)
    purchase_id = models.ForeignKey(PurchaseModel, on_delete=models.CASCADE, null=False)
    is_completed = models.BooleanField(default=False)
    duration_in_months = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        db_table = 'EMIDetails'