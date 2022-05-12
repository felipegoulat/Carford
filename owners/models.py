from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class OwnerModel(models.Model):
    
    name = models.CharField(max_length=255)
    doc_number = models.CharField(max_length=100, unique=True)
    sales_opportunity = models.BooleanField(default=True)
