from django.contrib.auth.models import User
from django.db import models
from core.models import Abstract

class Customer(Abstract):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=12, null=True)
    email = models.EmailField(max_length=100)
    profile_pic = models.ImageField(null=True, blank=True, default='default.png', upload_to='customer_profile')

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.name)

class Product(Abstract):

    class Category(models.TextChoices):
        INDOOR = "INDOOR"
        OUTDOOR = "OUT DOOR"           

    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=10, choices=Category.choices, default=Category.INDOOR)
    price = models.FloatField(null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name

class Order(Abstract):

    class Status(models.TextChoices):
        PENDING = "PENDING"
        OUT_FOR_DELIVERY = "OUT FOR DELIVERY"
        DELIVERED = "DELIVERED"

    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return "{} and {}".format(self.customer.name, self.product.name)            