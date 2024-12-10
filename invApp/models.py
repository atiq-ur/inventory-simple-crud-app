from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.name