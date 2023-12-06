from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_weapon = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
