from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
