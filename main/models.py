from django.core.validators import MinValueValidator
from django.db import models


class Gems(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    balance = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(limit_value=0.01)]
    )
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)



class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title