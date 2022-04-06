from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products(self):
        return Product.objects.all()

    @staticmethod
    def get_products_by_name(self):
        return Product.objects.filter(category=self.id)

    @staticmethod
    def get_products_by_categoryId(self):
        return Product.objects.filter(category=self.id)


class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=True)
    desc = models.TextField()
    price = models.IntegerField()
    backInStock = models.BooleanField(default=False)
    inStock = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    offerPercentage = models.TextField(default=0)
    offerPrice = models.IntegerField(default=0)
    offer_benefit = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)


class Order (models.Model):

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default='')

    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.today)
    time = models.TimeField(default=datetime.datetime.now().time())
    address = models.CharField(max_length=50, default="", blank=True)
    phone = models.CharField(max_length=50, default="", blank=True)
    status = models.BooleanField(default=False)

    @staticmethod
    def get_orders_by_customer(id):
        return Order.objects.filter(user=id).order_by('-time')

    def placeorder(self):
        self.save()


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=55)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
