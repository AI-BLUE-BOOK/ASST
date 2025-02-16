'''from django.shortcuts import render
from django.http import JsonResponse
from .models import Job

def job_list(request):
    jobs = list(Job.objects.all().values())
    return JsonResponse(jobs, safe=False)



from django.http import JsonResponse
import numpy as np
from pymongo import MongoClient

def get_avg_salary(request):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["your_database_name"]
    jobs_collection = db["jobs"]

    city = "YourCity"  # Replace with dynamic user input if needed
    jobs = list(jobs_collection.find({"location": city}, {"salary": 1, "_id": 0}))

    salaries = [job["salary"] for job in jobs if isinstance(job["salary"], (int, float))]

    if salaries:
        avg_salary = np.mean(salaries)
    else:
        avg_salary = 0

    return JsonResponse({"average_salary": avg_salary})
'''


from django.http import JsonResponse
from django.shortcuts import render
from .models import Job
import numpy as np

def job_list(request):
    jobs = list(Job.objects.all().values())
    return JsonResponse(jobs, safe=False)

def get_avg_salary(request):
    job_ids = request.GET.getlist("job_ids[]")  
    if not job_ids:
        return JsonResponse({"error": "No jobs selected"}, status=400)

    jobs = Job.objects.filter(id__in=job_ids).values_list("salary", flat=True)

    salaries = [salary for salary in jobs if isinstance(salary, (int, float))]

    avg_salary = np.mean(salaries) if salaries else 0

    return JsonResponse({"average_salary": avg_salary})
