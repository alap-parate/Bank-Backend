from django.db import models

class RecoveryOfficer(models.Model):
    name = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name