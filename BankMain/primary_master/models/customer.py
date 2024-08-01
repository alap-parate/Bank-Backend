from django.db import models
from .branch import BranchMaster
from .locations import State,Zone,District,Taluka,City
from django.contrib.auth import get_user_model
from .nominee import Nominee

User = get_user_model()

class Customer(models.Model):
    sex_choice = (
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    )
    caste_cat = (
        ('ST','ST'),
        ('SC','SC'),
        ('OBC','OBC'),
        ('EWS','EWS'),
        ('OPEN','OPEN'),
    )
    
    br_id = models.ForeignKey(BranchMaster,on_delete=models.PROTECT)
    courtesy = models.CharField(max_length=10)
    f_name = models.CharField(max_length=255)
    m_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    category = models.CharField(max_length=10,choices=(caste_cat))
    sex = models.CharField(max_length=1,choices=(sex_choice))
    age = models.IntegerField()
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10,null=True)
    caste = models.CharField(max_length=255)
    addr1 = models.CharField(max_length=255)
    addr2 = models.CharField(max_length=255)
    addr3 = models.CharField(max_length=255,null=True)
    state = models.ForeignKey(State,on_delete=models.PROTECT)
    district = models.ForeignKey(District,on_delete=models.PROTECT, related_name='cust_district')
    taluka = models.ForeignKey(Taluka,on_delete=models.PROTECT, related_name='cust_taluka')
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='cust_city')
    zone = models.ForeignKey(Zone,on_delete=models.PROTECT, related_name='cust_zone')
    pincode = models.CharField(max_length=6)
    
    company_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255) # service or business
    desig = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    office_id_no = models.CharField(max_length=50, null=True)
    mnt_income = models.IntegerField(null=True)
    oaddr1 = models.CharField(max_length=255)
    oaddr2 = models.CharField(max_length=255)
    oaddr3 = models.CharField(max_length=255, null=True)
    ocity = models.TextField()
    ophone1 = models.CharField(max_length=10)
    ophone2 = models.CharField(max_length=10, null=True)
    gstno = models.CharField(max_length=15, null=True)
    
    # native details
    paddr1 = models.CharField(max_length=255)
    paddr2 = models.CharField(max_length=255)
    paddr3 = models.CharField(max_length=255, null=True)
    pstate = models.ForeignKey(State,on_delete=models.PROTECT, related_name='pcust_state')
    pdistrict = models.ForeignKey(District,on_delete=models.PROTECT, related_name='pcust_district')
    ptaluka = models.ForeignKey(Taluka,on_delete=models.PROTECT, related_name='pcust_taluka')
    pcity = models.ForeignKey(City, on_delete=models.PROTECT, related_name='pcust_city')
    ppincode = models.CharField(max_length=6)
    birth_date = models.DateField()
    
    # document id numbers
    aadharno = models.CharField(max_length=12)
    panno = models.CharField(max_length=10)
    passportno = models.CharField(max_length=8)
    other = models.CharField(max_length=255)
    
    # document uploads
    aadhar_doc = models.FileField(upload_to='uploads/')
    pan_doc = models.FileField(upload_to='uploads/')
    passport_doc = models.FileField(upload_to='uploads/')
    other_doc = models.FileField(upload_to='uploads/')
    
    # house rent/ownership details
    h_type = models.CharField(max_length=50) # house type rent or ownership
    rent_vdate = models.DateField(null=True)
    
    # Account Confirmation 
    confirm = models.BooleanField(default=False)
    confirm_by = models.ForeignKey(User,null=True,on_delete=models.PROTECT,related_name='customer_confirm')
    confirm_time = models.DateTimeField(null=True)
    
    # Account Freeze
    freeze_acc = models.BooleanField(default=False)
    freeze_time = models.DateTimeField(null=True)
    
    # create/update time and user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='customer_created')
    updated_by = models.ForeignKey(User, null=True,on_delete=models.PROTECT,related_name='customer_updated')
    
    # Account merge
    merge_to = models.IntegerField(default=0)
    merge_by = models.IntegerField(default=0)
    merge_time = models.DateTimeField(null=True)
      
    # bank details
    bank_name = models.CharField(max_length=255)
    bank_acc = models.CharField(max_length=50)
    bank_ifsc = models.CharField(max_length=20)
    
    # nominee details
    nom_name = models.CharField(max_length=255)
    nom_rel = models.ForeignKey(Nominee, on_delete=models.PROTECT)
    nom_age = models.IntegerField()
    nom_addr1 = models.CharField(max_length=255)
    nom_addr2 = models.CharField(max_length=255)
    nom_city = models.CharField(max_length=100)
    nom_pincode = models.CharField(max_length=6)