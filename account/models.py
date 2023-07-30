from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

# Create your models here.

class CustomUserManager(UserManager):
    def custom_user(self, name, email, password, **extra_field):
        if not email:
            raise ValueError("Please enter correct Email")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, name=None, email=None, password=None, **extra_field):
        extra_field.setdefault('is_staff', False)
        extra_field.setdefault('is_superuser', False)

        return self.custom_user(name, email, password, **extra_field)
    
    def create_superuser(self, name=None, email=None, password=None, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)

        return self.custom_user(name, email, password, **extra_field)
    

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=100, blank=True, default='')
    avatar = models.ImageField(upload_to='media/avatars', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []