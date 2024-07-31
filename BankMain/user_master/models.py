from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.timezone import now

class UserAccountManager(BaseUserManager):
    def create_user(self,role, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, email, password=None, **extra_fields):
        user = self.create_user(email, name, password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    def create_employee(self, name, email, password=None, **extra_fields):
        user = self.create_user(email, name, password, **extra_fields)
        user.save(using=self._db)
        return user
    

class UserAccount(AbstractBaseUser, PermissionsMixin):
    Roles = (
    ("superadmin","Super Admin"),
    ("admin", "Admin"),
    ("employee", "Employee"),
)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=10, choices=(Roles))
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=now, blank=True)
    login_ip = models.CharField(max_length=45, default='none')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','role']
    
    def get_fullname(self):
        return self.name
    
    def __str__(self):
        return self.email
