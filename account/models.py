from django.db import models

class UID(models.Model):
    uid = models.IntegerField(max_length=66)