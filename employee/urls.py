
from django.urls import path
from .views import (
    ListEmployees, 
    EditEmployees,
    DeleteEmployees,
    CreateEmployess,
    )

urlpatterns = [
    path('list-employees/', ListEmployees.as_view(), name='list_employess'),
    path('edit-employees/<int:pk>/', EditEmployees.as_view(), name='edit_employess'),
    path('delete-employees/<int:pk>/', DeleteEmployees.as_view(), name='delete_emplyess'),
    path('create-employees/', CreateEmployess.as_view(), name='create_employees'),
]
