from django.db import models
from .branch import BranchMaster
from .general_ledger import GL_Master
from .nominee import Nominee
from django.contrib.auth import get_user_model

User = get_user_model()

class FixedDepositMaster(models.Model):
    br_id = models.ForeignKey(BranchMaster,on_delete=models.PROTECT)
    gl_id = models.ForeignKey(GL_Master,on_delete=models.PROTECT)
    acc_no = models.IntegerField()
    opamnt = models.DecimalField(decimal_places=2, max_digits=10)
    opdate = models.DateField()
    asondate = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    intrate = models.DecimalField(decimal_places=2, max_digits=10)
    dueamnt = models.DecimalField(decimal_places=2, max_digits=10)
    cert_no = models.IntegerField()
    agcd = models.IntegerField()
    instruction = models.TextField(null=True)
    intro_id = models.IntegerField()
    
    close_date = models.DateField(null=True)
    isactive = models.BooleanField(default=True)
    
    nom_name = models.CharField(max_length=255)
    nom_rel = models.ForeignKey(Nominee,on_delete=models.PROTECT)
    nom_age = models.IntegerField()
    nom_addr1 = models.CharField(max_length=255)
    nom_addr2 = models.CharField(max_length=255)
    nom_city = models.CharField(max_length=100)
    nom_pincode = models.CharField(max_length=6) 
    
    # created/updated
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT)