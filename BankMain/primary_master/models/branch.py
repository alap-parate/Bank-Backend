from django.db import models
from .locations import State,District,Taluka,Zone

class BranchMaster(models.Model):
    title = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=10)
    short_code = models.CharField(max_length=10)
    start_date = models.DateField()
    addr1 = models.CharField(max_length=255)
    addr2 = models.CharField(max_length=255)
    addr3 = models.CharField(max_length=255)
    state = models.ForeignKey(State,on_delete=models.PROTECT)
    district = models.ForeignKey(District,on_delete=models.PROTECT)
    taluka = models.ForeignKey(Taluka,on_delete=models.PROTECT)
    zone = models.ForeignKey(Zone,on_delete=models.PROTECT)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)