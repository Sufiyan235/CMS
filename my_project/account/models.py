from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,password=None):
        if not email:
            raise ValueError("User must have an email address")


        user=self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active=True
        user.is_staff=True
        user.set_password(password)#set_passwrd()is use to set password in encrypted manner
        user.save(using=self._db)
        return user
    
    def create_masteruser(self,first_name,last_name,email,company_name,password=None):

        user=self.model(
            email=self.normalize_email(email),   
            first_name=first_name,
            # designation=designation,
            # phone_number=phone_number,
            last_name=last_name,
            company_name=company_name,
        )
        user.is_active=True
        user.is_staff=True
        user.is_admin = True
        user.is_master_admin = True
        user.is_super_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    # phone_number=models.CharField(max_length=20)
    company_name=models.CharField(max_length=100)
    date_joined=models.DateTimeField(auto_now_add=True)
    # designation=models.CharField(max_length=100,null=True,blank=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_master_admin=models.BooleanField(default=False)
    is_super_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    # is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    def has_perm(self,perm,obj=None):
        return self.is_admin

    objects=MyAccountManager()

    def has_module_perms(self,add_label):
        return True
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    # @property
    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"


