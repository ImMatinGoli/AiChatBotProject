from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to='users_photos/', null=True, blank=True, default='users_photos/default.png')

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.username}'
