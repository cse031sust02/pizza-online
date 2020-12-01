from authentication.models import CustomUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Owner(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Restaurant(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=50)
    logo = models.CharField(max_length=150)
    website = models.CharField(max_length=80)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    image = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Order(models.Model):

    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        DELIVERED = 'delivered', _('Delivered')
        REJECTED = 'rejected', _('Rejected')

    order_no = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_no
