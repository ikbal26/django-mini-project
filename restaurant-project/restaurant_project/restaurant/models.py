from django.db import models
from django.contrib.auth.models import User

# Категории (Пицца, Суши, Напитки)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Блюда
class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Бронирование столиков
class TableBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    booking_time = models.DateTimeField()

    def __str__(self):
        return f"Столик {self.table_number} - {self.user.username}"
