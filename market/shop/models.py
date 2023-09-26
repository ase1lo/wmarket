from django.db import models

# Create your models here.
from users.models import CustomUser


class Product(models.Model):
    title = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.title


class UserProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    sell = 'SL'
    buy = 'BU'
    want_to = [
        (sell, 'sell'),
        (buy, 'buy'),
    ]
    want = models.CharField(max_length=2, choices=want_to, default=buy)

    def __str__(self) -> str:
        return str(self.product)


