from django.urls import path
from .views import job_list
from .views import get_avg_salary

urlpatterns = [
    path('jobs/', job_list, name='job_list'),
    path('get_avg_salary/', get_avg_salary, name='get_avg_salary'),
]
