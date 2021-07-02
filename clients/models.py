from django.db import models
from cpf_field.models import CPFField
from django.urls import reverse


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    cpf = CPFField('cpf')
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    def get_absolute_url(self):
        return reverse('list_clients')


    def get_full_phone_number(self):
        return f'({self.area_code}) {self.phone_number}'


    def get_name(self):
        return f'{self.first_name} {self.last_name}'


    def get_cpf(self):
        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'


    def get_full_city(self):
        return f'{self.city} - {self.state}'


    class Meta:
        db_table = 'clients'

