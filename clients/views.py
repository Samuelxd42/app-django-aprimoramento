
from django.views.generic import (
    ListView, 
    UpdateView, 
    DeleteView, 
    CreateView
    )

from .models import Client
from django.urls import reverse_lazy


class ListClients(ListView):
    model = Client
    queryset = Client.objects.all()


class EditClients(UpdateView):
    model = Client
    fields = ['first_name', 'last_name', 'email', 'cpf', 
        'birth_date', 'area_code', 'phone_number', 'country',
        'state', 'city']


class DeleteClients(DeleteView):
    model = Client
    success_url = reverse_lazy('list_clients')


class CreateClients(CreateView):
    model = Client
    fields = fields = ['first_name', 'last_name', 'email', 'cpf', 
        'birth_date', 'area_code', 'phone_number', 'country',
        'state', 'city']
    success_url = reverse_lazy('list_clients')

