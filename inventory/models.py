from django.db import models

# Create your models here.

class Truck(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class IceCream(models.Model):

    name = models.CharField(max_length=50)
    flavours = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    truck_id = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True, blank=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ShavedIce(models.Model):

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    truck_id = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True, blank=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SnackBar(models.Model):

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    truck_id = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True, blank=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name
