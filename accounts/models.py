from django.db import models
from django.contrib.auth.models import User

# Roles
class UserType(models.Model):
    name = models.CharField(max_length=30)

# Rol para cada usuario
class UserProfile(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    type = models.ForeignKey(UserType, null=False, on_delete=models.PROTECT)
