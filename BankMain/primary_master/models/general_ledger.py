from django.db import models

class Acc_type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Group_Master(models.Model):
    Choices = (
        ("B","Balance Sheet"),
        ("P","P&L")
    )

    name = models.CharField(max_length=100)
    pl_bl = models.CharField(max_length=1,choices=(Choices))
    
    def __str__(self):
        return self.name
    
class GL_Master(models.Model):
    Choices = (
        ("B","Balance Sheet"),
        ("P","P&L")
    )
    
    Intr_Choices = (
        (1,"Quartly"),
        (2,"Yearly"),
        (3,"Flat")
    )

    gl_id = models.AutoField(primary_key=True,)
    master_gl = models.IntegerField(null=True)
    title = models.CharField(max_length=100, unique=True)
    acc_code = models.CharField(max_length=10,unique=True)
    pl_bl = models.CharField(max_length=1,choices=(Choices))
    acc_type = models.ForeignKey(Acc_type, on_delete=models.PROTECT, related_name="acc_type")
    group_id = models.ForeignKey(Group_Master, on_delete=models.PROTECT,related_name='group_name')
    int_code = models.IntegerField(default=0,null=True)
    pr_int_code = models.IntegerField(default=0, null=True)
    due_amnt = models.DecimalField(default=0)
    int_cal_type = models.DecimalField(default=0)
    due_cal_type = models.DecimalField(default=0)
    pen_cl_type = models.IntegerField(default=0)
    ag_cd = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title