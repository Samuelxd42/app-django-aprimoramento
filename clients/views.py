
from .form import CustumerForm
from django.views.generic import (
    ListView, 
    UpdateView, 
    DeleteView, 
    CreateView
    )

from .models import Client
from django.urls import reverse_lazy
from django.db.models import Q



class ListClients(ListView):
    model = Client
    paginate_by = 4
    
    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=name) | 
                Q(last_name__icontains=name) | 
                Q(phone_number__icontains=name) |
                Q(cpf__icontains=name)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class EditClients(UpdateView):
    model = Client
    form_class = CustumerForm



class DeleteClients(DeleteView):
    model = Client
    success_url = reverse_lazy('list_clients')


class CreateClients(CreateView):
    model = Client
    success_url = reverse_lazy('list_clients')
    form_class = CustumerForm

