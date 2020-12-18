from django.db import models

class ValidationModel(models.Model):
    synonym = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    answer = models.BooleanField(null=True)
    comment = models.CharField(max_length=255)
