from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Job

def home(request):
    jobs = Job.objects.all()  # Fetch jobs from MongoDB Atlas
    #return render(request, "home.html", {"jobs": jobs})  # Pass jobs to template
    return render(request, "index.html", {"jobs": jobs})  



urlpatterns = [
    path("", home, name="home"),
   # path("", index,name="index"),
    path("admin/", admin.site.urls),
    path("jobs/", include("jobs.urls")),
]