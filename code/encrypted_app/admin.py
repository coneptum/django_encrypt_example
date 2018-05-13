from django.contrib import admin
from .models import ModelWithSomeEncryptedFields

@admin.register(ModelWithSomeEncryptedFields)
class ModelWithSomeEncryptedFieldsAdmin(admin.ModelAdmin):
    list_display = ['non_encrypted_field', 'encrypted_field']