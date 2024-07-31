from django.db import models
from .locations import State,District,Taluka
from .general_ledger import GL_Master

class Society(models.Model):
    name = models.CharField(max_length=255)
    reg_no = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    reg_addr1 = models.CharField(max_length=255)
    reg_addr2 = models.CharField(max_length=255)
    reg_addr3 = models.CharField(max_length=255)
    head_addr1 = models.CharField(max_length=255)
    head_addr2 = models.CharField(max_length=255)
    head_addr3 = models.CharField(max_length=255)
    start_date = models.DateField()
    state = models.ForeignKey(State,on_delete=models.PROTECT,related_name='state')
    district = models.ForeignKey(District,on_delete=models.PROTECT,related_name='district')
    taluka = models.ForeignKey(Taluka,on_delete=models.PROTECT,related_name='taluka')
    city = models.CharField(max_length=255)
    
    logo_file = models.FileField(upload_to='uploads/')
    letter_head = models.FileField(upload_to='uploads/')
    
    gstno = models.CharField(max_length=15)
    
    comm_glid = models.ForeignKey(GL_Master)
    tds_glid = models.ForeignKey(GL_Master)
    ag_tds_glid = models.ForeignKey(GL_Master)
    stationary_glid = models.ForeignKey(GL_Master)
    charges_glid = models.ForeignKey(GL_Master)
    sgst_per = models.DecimalField()
    cgst_per = models.DecimalField()