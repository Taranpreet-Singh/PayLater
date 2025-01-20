from django.db import models
from .user import UserModel

class PurchaseModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    purchase_id = models.BigAutoField(primary_key=True)
    ammount = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def isValidForPurchase(self):
        if self.ammount < self.user_id.credit_limit:
            return True
        return False

    class Meta:
        db_table = 'PurchaseDetails'