from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    users = models.ManyToManyField(get_user_model(), related_name='products')

    def __str__(self):
        return self.description
