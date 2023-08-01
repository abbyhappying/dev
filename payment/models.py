from django.db import models

from django.contrib.auth.models import User

from store.models import Products

# Create your models here.
class ShipppingAddress(models.Model):

    full_name = models.CharField(max_length = 300)

    email = models.EmailField(max_length=255)

    address1 = models.CharField(max_length=300)

    address2 = models.CharField(max_length=300)

    city = models.CharField(max_length = 255)

    state = models.CharField(max_length=255, null=True, blank=True)

    zipcode = models.CharField(max_length=255, null=True, blank=True)

    # defines a foreign key relationship between the ShippingAddress and the User model(1 user to many address )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)

    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self):

        return 'Shipping Address -' + str(self.id)

class Order(models.Model):

    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=255)
    shipping_address = models.TextField(max_length=100000)
    amount_paid = models.DecimalField(max_digits=8,decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)

    def __str__(self):

        return 'order-#'+str(self.id)

class OrderItem(models.Model):
    # use foreignkey connect order model with order items model, relation 1 to many
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):

        return 'Order Item -#' + str(self.id)
