
from django.urls import path
from .views import (
    ListClients, 
    EditClients, 
    DeleteClients, 
    CreateClients)

urlpatterns = [
    path('list-clients/', ListClients.as_view(), name='list_clients'),
    path('edit-clients/<int:pk>', EditClients.as_view(), name='edit_clients'),
    path('delete-clients/<int:pk>', DeleteClients.as_view(), name='delete_clients'),
    path('create-clients/', CreateClients.as_view(), name='create_clients')
]
