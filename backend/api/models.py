from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, last_name, location, introduction, about, github, linked_in, phone_number, password=None, **other_fields ):
        if not email:
            raise ValueError('Please provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name, location=location, introduction=introduction, about=about, github=github, linked_in=linked_in, phone_number=phone_number, **other_fields)
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, user_name, first_name, last_name, location, introduction, about, github, linked_in, phone_number, password=None, **other_fields ):

        # setting superuser status
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if not email:
            raise ValueError('Please provide an email address')
        email = self.normalize_email(email)
        superuser = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name, location=location, introduction=introduction, about=about, github=github, linked_in=linked_in, phone_number=phone_number, **other_fields)
        
        superuser.set_password(password)
        superuser.save()
        return superuser

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email Address', max_length=50, unique=True)
    user_name = models.CharField(max_length=50)
    first_name  = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    introduction = models.CharField(max_length=255)
    about = models.TextField()
    profile_picture = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.CharField(max_length=100, null=True, blank=True)
    github = models.CharField(max_length=100)
    linked_in = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    created_at = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name', 'location', 'introduction', 'about', 'github', 'linked_in', 'phone_number']

    def __str__(self):
        return self.email


