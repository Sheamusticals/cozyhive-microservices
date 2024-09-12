from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_host = models.BooleanField(default=False)

    def __str__(self):
        return self.username
