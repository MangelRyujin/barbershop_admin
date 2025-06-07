from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to="users")
    is_worker = models.BooleanField(default=False)
    # add additional fields in here

    def __str__(self):
        return self.username