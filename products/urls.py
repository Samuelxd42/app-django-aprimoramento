
from clients.views import EditClients
from django.urls import path
from .views import (
    ListProducts,
    CreateProducts,
    EditProducts,
    DeleteProducts
)

urlpatterns = [
    path('list-products/', ListProducts.as_view(), name='list_products'),
    path('edit-products/<int:pk>/', EditProducts.as_view(), name='edit_products'),
    path('delete-products/<int:pk>/', DeleteProducts.as_view(), name='delete_products'),
    path('create-products/', CreateProducts.as_view(), name='create_products'),
]