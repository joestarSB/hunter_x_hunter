from django.db import models

class UID(models.Model):
    uid = models.CharField(max_length=66)