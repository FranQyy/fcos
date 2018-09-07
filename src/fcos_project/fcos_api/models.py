from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
  #Enable Django work with our user model
  def create_user(self, email, first_name, last_name, city, password=None, **extra_fields):
    if not email:
      raise ValueError('Provide email address!')

    email = self.normalize_email(email)
    user = self.model(email=email, first_name=first_name, last_name=last_name, city=city, **extra_fields)

    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self, email, first_name, last_name, city, password=None, **extra_fields):
    #creates superuser
    user = self.create_user(email, first_name, last_name, city, **extra_fields)

    user.is_superuser = True
    user.is_staff = True

    user.save(using=self._db)

    return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
  #That's user profile in our app
  email = models.EmailField(max_length=255, unique=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserProfileManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'city']

  def get_full_name(self):
    #It return the first and the second name
    return self.first_name + ' ' + self.second_name

  def get_short_name(self):
    #It return 3 letters of the first_name concatenated with 3 letters of the second_name
    return self.first_name[:2] + self.second_name[:2]

  def __str__(self):
    return self.email
