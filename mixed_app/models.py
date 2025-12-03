from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    color = models.CharField(max_length=30)
    price = models.IntegerField()
    is_new = models.BooleanField()


class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()

class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.IntegerField()
    adress = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"

