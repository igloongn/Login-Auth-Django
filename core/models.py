from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email=models.EmailField(max_length=50, null=True, blank=True)    
    firstname=models.CharField(max_length=20, null=True, blank=True)
    lastname=models.CharField(max_length=20, null=True, blank=True)
    level=models.CharField(max_length=20, null=True, blank=True)
    school=models.CharField(max_length=20, null=True, blank=True)
    

    def __str__(self):
        return self.user.username
