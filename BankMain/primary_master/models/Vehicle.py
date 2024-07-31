from django.db import models
from .general_ledger import GL_Master
from django.contrib.auth import get_user_model

User = get_user_model()

class VehicleMaster(models.Model):
    gl_id = models.ForeignKey(GL_Master)
    acc_no = models.IntegerField()
    v_type = models.CharField(max_length=255)
    v_year = models.DateField()
    model = models.DateField()
    v_reg_no = models.CharField(max_length=50)
    v_chas_no = models.CharField(max_length=20)
    v_eng_no = models.CharField(max_length=20)
    permit_no = models.CharField(max_length=50)
    policy_no = models.CharField(max_length=50)
    insu_no = models.CharField(max_length=50)
    remark = models.TextField(null=True)
    plcy_rdate = models.DateField()
    prmt_rdate = models.DateField()
    v_owner = models.CharField(max_length=255)
    v_add1 = models.CharField(max_length=255)
    v_add2 = models.CharField(max_length=255)
    v_tel = models.CharField(max_length=10)