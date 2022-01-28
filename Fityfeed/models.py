from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    OPTIONS = (
        ('breakfast','breakfast'),
        ('lunch', 'lunch'),
        ('dinner','dinner'),
        ('snacks', 'snacks'),
    )

    name = models.CharField(max_length=128, choices=OPTIONS)

    def __str__(self):
        return self.name


class Fooditem(models.Model):
    name = models.CharField(max_length=128)
    category = models.ManyToManyField(Category)
    carbonhydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=2 ,default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calorie = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    quantity = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return self.name


class UserFooditem(models.Model):
    customer = models.ManyToManyField(Customer, blank=True)
    fooditem = models.ManyToManyField(Fooditem)