
from products.models import Product
from .forms import CustumerFormProducts
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (
    ListView, 
    UpdateView, 
    DeleteView, 
    CreateView
    )


class ListProducts(ListView):
    model = Product
    paginate_by = 4

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            object_list = self.model.objects.filter(
                Q(name__icontains=name)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class EditProducts(UpdateView):
    model = Product
    form_class = CustumerFormProducts


class CreateProducts(CreateView):
    model = Product
    form_class = CustumerFormProducts


class DeleteProducts(DeleteView):
    model = Product
    success_url = reverse_lazy('list_products')

