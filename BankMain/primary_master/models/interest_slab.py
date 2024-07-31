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
    gl_id = models.ForeignKey(GL_Master)
    fr = models.IntegerField()
    upto = models.IntegerField()
    int_rate = models.DecimalField()
    sr_int_rate = models.DecimalField()
    status = models.BooleanField(default=True)
    
    created_by  = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    close_by = models.ForeignKey(User,null=True)
    close_date = models.DateTimeField(null=True)