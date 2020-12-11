from django.db import models

class ValidationDB(models.Model):
    synonym = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    answer = models.CharField(max_length=4)
