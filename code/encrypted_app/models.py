from django.db import models
from django_cryptography.fields import encrypt


class ModelWithSomeEncryptedFields(models.Model):
    non_encrypted_field = models.CharField(max_length=100)
    encrypted_field = encrypt(models.CharField(max_length=100))
