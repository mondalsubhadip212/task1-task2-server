from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=150,null=False,blank=False,unique=True)
    username = models.CharField(max_length=150,null=False,blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username

class UserDetails(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=500,null=True)
    company_name = models.CharField(max_length=150,null=True)
    brand = models.CharField(max_length=150,null=True)
    client_type = models.CharField(max_length=150,null=True)
    # avg revenue in lakhs i.e -> 50 lakhs
    avg_revenue = models.FloatField(null=True)

    def __str__(self):
        return self.user.username