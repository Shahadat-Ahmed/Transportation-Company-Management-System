from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, uname,uid,nid,email,phone,license_no,license_renewed,specialization,experience,address,password=None):#uname,uid, nid,email,phone,bank,address,pass1//////self, email, password=None, **extra_fields
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(Driver_name=uname,user_id=uid,NID=nid,email=email,phone=phone,license_no=license_no,license_renewed=license_renewed,specialization=specialization,experience=experience,address=address)#vehicle_id=vehicle_id
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,uname,uid,nid,email,phone,license_no,license_renewed,specialization,experience,address,password=None):
        #extra_fields.setdefault('vehicle_id', 'Not appointed')
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(uname,uid,nid,email,phone,license_no,license_renewed,specialization,experience,address,password=password)

class MyUser(AbstractBaseUser):
    Driver_name = models.CharField(max_length=255)
    user_id = models.CharField(unique=True, max_length=255)
    NID = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    license_no = models.TextField()
    license_renewed = models.DateTimeField()
    specialization = models.TextField()
    experience = models.TextField()
    address = models.TextField()
    #vehicle_id = models.TextField(default=None)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Driver_name', 'user_id', 'NID', 'phone', 'license_no', 'license_renewed', 'specialization', 'experience','address']

    def __str__(self):
        return self.email