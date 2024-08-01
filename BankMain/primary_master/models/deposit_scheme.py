from django.db import models
from .general_ledger import GL_Master
from django.contrib.auth import get_user_model

User = get_user_model()

class DepositScheme(models.Model):
    title = models.CharField(max_length=255)
    gl_id = models.ForeignKey(GL_Master,on_delete=models.PROTECT)
    days = models.IntegerField()
    months = models.IntegerField()
    int_rate = models.DecimalField(decimal_places=2, max_digits=10)
    start_date = models.DateField()
    end_date = models.DateField()
    
    created_by  = models.ForeignKey(User,on_delete=models.PROTECT, related_name='depo_createdby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    close_by = models.ForeignKey(User,null=True,on_delete=models.PROTECT, related_name='depo_closeby')
    close_date = models.DateTimeField(null=True)