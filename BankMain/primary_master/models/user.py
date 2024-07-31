from django.db import models
from .locations import State, District, Taluka
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    f_name = models.CharField(max_length=255,null=True)
    l_name = models.CharField(max_length=255,null=True)
    father_name = models.CharField(max_length=255,null=True)
    mother_name = models.CharField(max_length=255,null=True)
    dob = models.DateField(null=True)
    address = models.TextField(null=True)
    state = models.ForeignKey(State,null=True)
    district = models.ForeignKey(District,null=True)
    Taluka = models.ForeignKey(Taluka,null=True)
    pincode = models.CharField(max_length=6,null=True)
    phoneno = models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=255, null=True)
    marital_status = models.CharField(max_length=50,null=True)
    branch_id = models.IntegerField(null=True)
    
    aadharno = models.CharField(max_length=12,null=True)
    aadhar_doc = models.FileField(upload_to='uploads/')
    panno = models.CharField(max_length=10,null=True)
    pan_doc = models.FileField(upload_to='uploads/')
        
    education_type = models.CharField(max_length=255,null=True)
    course = models.CharField(max_length=255,null=True)
    specialization = models.CharField(max_length=255,null=True)
    university = models.CharField(max_length=255,null=True)
    doc = models.DateField(null=True)
    is_highest_degree = models.BooleanField(default=True)
    
    position = models.CharField(max_length=255,null=True)
    department = models.CharField(max_length=255,null=True)
    start_date = models.DateField(null=True)
    emp_type = models.DateField(null=True)
    work_mail = models.CharField(max_length=255,null=True)
    work_phone = models.CharField(max_length=10,null=True)