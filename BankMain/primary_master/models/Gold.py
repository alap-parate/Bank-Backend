from django.db import models
from .general_ledger import GL_Master
from django.contrib.auth import get_user_model

User = get_user_model()

class GoldMaster(models.Model):
    gl_id = models.ForeignKey(GL_Master)
    acc_no = models.IntegerField()
    particular = models.CharField(max_length=100)
    qty = models.IntegerField()
    net_weight = models.DecimalField()
    net_valuation = models.DecimalField()
    
    # created/updated
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)