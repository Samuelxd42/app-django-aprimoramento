from django.db import models
from .forms import CustumerFormEmployee
from django.views.generic import (
    ListView, 
    UpdateView, 
    DeleteView, 
    CreateView
    )

from .models import Employee
from django.urls import reverse_lazy
from django.db.models import Q


class ListEmployees(ListView):
    model = Employee
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


class EditEmployees(UpdateView):
    model = Employee
    form_class = CustumerFormEmployee


class DeleteEmployees(DeleteView):
    model = Employee
    success_url = reverse_lazy('list_employess')


class CreateEmployess(CreateView):
    model = Employee
    form_class =  CustumerFormEmployee
