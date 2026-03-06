from .views import employee_query
from django.urls import path
urlpatterns = [
    path('employee_query/', employee_query, name='employee_query'),
]