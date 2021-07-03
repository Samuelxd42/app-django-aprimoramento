from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    
    def get_absolute_url(self):
        return reverse('list_products')


    class Meta:
        db_table = 'products'


    def __str__(self):
        return self.name
