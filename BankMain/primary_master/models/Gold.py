from django.db import models
from .general_ledger import GL_Master
from django.contrib.auth import get_user_model

User = get_user_model()

class GoldMaster(models.Model):
    gl_id = models.ForeignKey(GL_Master, on_delete=models.PROTECT)
    acc_no = models.IntegerField()
    particular = models.CharField(max_length=100)
    qty = models.IntegerField()
    net_weight = models.DecimalField(decimal_places=3, max_digits=10)
    net_valuation = models.DecimalField(decimal_places=3, max_digits=10)
    
    # created/updated
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)