import uuid
import base64
import hashlib
import os
from django.db import models
from django.contrib.auth.hashers import make_password


def secure_rand(length=8):
    token = os.urandom(length)
    return base64.b64encode(token)


class Users(models.Model):
    # id = models.IntegerField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    referral = models.CharField(max_length=100, null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def save(self, *args, **kwargs):
        if not self.referral:
            self.referral = secure_rand()

        self.password = make_password(self.password)
        super().save(*args, **kwargs)
