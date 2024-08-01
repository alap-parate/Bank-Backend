from django.db import models
from .general_ledger import GL_Master
from django.contrib.auth import get_user_model

User = get_user_model()

class InterestSlab(models.Model):

    dM = (
        ('Month','Month'),
        ('Days','Days')
    )
    
    dayMonth = models.CharField(max_length=10, choices=(dM))
    gl_id = models.ForeignKey(GL_Master, on_delete=models.PROTECT)
    fr = models.IntegerField()
    upto = models.IntegerField()
    int_rate = models.DecimalField(decimal_places=2, max_digits=10)
    sr_int_rate = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.BooleanField(default=True)
    
    created_by  = models.ForeignKey(User, on_delete=models.PROTECT,related_name='int_createdby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    close_by = models.ForeignKey(User,null=True, on_delete=models.PROTECT,related_name='int_closeby')
    close_date = models.DateTimeField(null=True)