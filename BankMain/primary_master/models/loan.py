from django.db import models
from .branch import BranchMaster
from .general_ledger import GL_Master
from .nominee import Nominee
from django.contrib.auth import get_user_model

User = get_user_model()

dm = (
    ('month','month'),
    ('day','day')
)

class FixedDepositMaster(models.Model):
    br_id = models.ForeignKey(BranchMaster)
    gl_id = models.ForeignKey(GL_Master)
    acc_no = models.IntegerField()
    loan_purpose = models.TextField()
    opamnt = models.DecimalField()
    opdate = models.DateField()
    meetdate = models.DateField()
    inst_from = models.DateField()
    no_of_inst = models.IntegerField()
    dM = models.CharField(max_length=5, choices=(dm))
    intrate = models.DecimalField()
    intamnt = models.DecimalField()
    sro_no = models.IntegerField()
    agcd = models.IntegerField()
    instruction = models.TextField(null=True)
    mortgage_detail = models.TextChoices()
    valuation = models.DecimalField()
    mortage_date = models.DateField()
    guarantor_1 = models.IntegerField(null=True)
    guarantor_2 = models.IntegerField(null=True)
    guarantor_3 = models.IntegerField(null=True)
    guarantor_4 = models.IntegerField(null=True)
    
    recommended_by = models.IntegerField(null=True)
    saving_no = models.CharField(max_length=100)
    
        
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
    created_by = models.ForeignKey(User)