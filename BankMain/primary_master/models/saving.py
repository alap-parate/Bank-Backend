from django.db import models
from .branch import BranchMaster
from .general_ledger import GL_Master
from .nominee import Nominee
from django.contrib.auth import get_user_model

User = get_user_model()

class SavingDepositMaster(models.Model):
    br_id = models.ForeignKey(BranchMaster,on_delete=models.PROTECT)
    gl_id = models.ForeignKey(GL_Master,on_delete=models.PROTECT)
    acc_no = models.IntegerField()
    opdate = models.DateField()
    agcd = models.IntegerField()
    lockamnt = models.DecimalField(decimal_places=2, max_digits=10)
    instruction = models.TextField(null=True)
    intro_id = models.IntegerField()
    
    isactive = models.BooleanField(default=True)
    
    nom_name = models.CharField(max_length=255)
    nom_rel = models.ForeignKey(Nominee, on_delete=models.PROTECT)
    nom_age = models.IntegerField()
    nom_addr1 = models.CharField(max_length=255)
    nom_addr2 = models.CharField(max_length=255)
    nom_city = models.CharField(max_length=100)
    nom_pincode = models.CharField(max_length=6)
    
    close_date = models.DateField(null=True)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)