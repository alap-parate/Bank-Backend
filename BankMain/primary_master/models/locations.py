from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='districts')
    
    def __str__(self):
        return f"{self.name}, {self.state.name}"
    
class Taluka(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.PROTECT, related_name='talukas')
    
    def __str__(self):
        return f"{self.name}, {self.district.name}"