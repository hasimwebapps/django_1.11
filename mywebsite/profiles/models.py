import uuid
import base64
import os
from django.db import models


def secure_rand(length=8):
    token = os.urandom(length)
    return base64.b64encode(token)


class Users(models.Model):
    # id = models.IntegerField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    referral = models.CharField(max_length=100, null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def save(self, *args, **kwargs):
        #### How can I alter here the ImageField parameters?
        if not self.referral:
            self.referral = secure_rand()
        print(self.referral)
        super().save(*args, **kwargs)
