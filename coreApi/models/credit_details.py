from django.db import models
from .user import UserModel

class CreditDetailsModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    credit_id = models.BigAutoField(primary_key=True)
    max_credit_limit = models.IntegerField(default=0)
    credit_limit = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'CreditDetails'