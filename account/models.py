from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, company_name, phone_number, password=None):
        if not email:
            raise ValueError("Email is required")
        if not company_name:
            raise ValueError("company name id required")
        if not phone_number:
            raise ValueError('Please provide an active phone number')


        user = self.model(
            email =  self.normalize_email(email),
            company_name = company_name,
            phone_number = phone_number,         
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, company_name, phone_number, password = None):
        user = self.create_user(
            email = self.normalize_email(email),
            company_name = company_name,
            phone_number = phone_number,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=60, unique=True)
    company_name = models.CharField(verbose_name="company name", max_length=200, unique=True)
    phone_number = models.CharField(max_length=14, verbose_name="phone_number")
    date_joined = models.DateTimeField(verbose_name = "date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active =  models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)    

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['company_name', 'phone_number']


    objects = MyUserManager()


    def __str__(self):
        return self.company_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

