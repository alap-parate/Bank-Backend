from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.name}, {self.state.name}"
    
class Taluka(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.name}, {self.district.name}"
    
class City(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.PROTECT, default=None)
    taluka = models.ForeignKey(Taluka, on_delete=models.PROTECT, default=None)
    
    def __str__(self):
        return f"{self.name}, {self.state.name}"
    
class Zone(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
  
    def __str__(self):
        return f"{self.name}, {self.state.name}"