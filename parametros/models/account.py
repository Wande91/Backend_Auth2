from django.db import models
from .user     import user

class Account(models.Model):
    id                  = models.AutoField(primary_key=True)
    user                = models.ForeignKey(user, related_name='account', on_delete=models.CASCADE)
    balance             = models.IntegerField(default=0)
    last_change_date    = models.DateTimeField()
    is_active           = models.BooleanField(default=True)