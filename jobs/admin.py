
'''from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib import messages
from .models import Job
import numpy as np

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'company', 'location', 'salary', 'rating', 'job_actions')
    search_fields = ('position_name', 'company', 'location')
    list_filter = ('company', 'location', 'rating')
    ordering = ('position_name',)
    actions = ['calculate_average_salary_by_city']

    def job_actions(self, obj):
        """
        Generates the Edit and Delete buttons for each job entry.
        """
        edit_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=[obj.pk])
        delete_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete', args=[obj.pk])

        return format_html(
            '<a href="{}" style="margin-right: 5px; padding: 5px 10px; background-color: #007bff; color: white; border-radius: 5px; text-decoration: none;">Edit</a>'
            '<a href="{}" style="padding: 5px 10px; background-color: #dc3545; color: white; border-radius: 5px; text-decoration: none;">Delete</a>',
            edit_url, delete_url
        )

    job_actions.short_description = 'Actions'

    def calculate_average_salary_by_city(self, request, queryset):
        """
        Admin action to calculate the average salary for each selected city's jobs.
        """
        city_salaries = {}

        for job in queryset:
            if isinstance(job.salary, (int, float)):  # Ensure salary is numeric
                city_salaries.setdefault(job.location, []).append(job.salary)

        if city_salaries:
            message_lines = ["Average Salaries by City:"]
            for city, salaries in city_salaries.items():
                avg_salary = np.mean(salaries)
                message_lines.append(f"{city}: ${avg_salary:.2f}")

            self.message_user(request, "\n".join(message_lines), messages.SUCCESS)
        else:
            self.message_user(request, "No valid salaries found in the selection.", messages.WARNING)

    calculate_average_salary_by_city.short_description = "Calculate AVG Salary by City"

# Customizing the Django Admin Panel Titles
admin.site.site_header = "Job Portal Admin"
admin.site.site_title = "Job Management"
admin.site.index_title = "Manage Jobs"
'''


from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib import messages
from django.db.models import Avg
from .models import Job
import numpy as np
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'company', 'location', 'salary', 'rating', 'job_actions')
    search_fields = ('position_name', 'company', 'location')
    list_filter = ('company', 'location', 'rating')
    ordering = ('position_name',)
    actions = ['calculate_average_salary_by_city']

    def job_actions(self, obj):
        """
        Generates the Edit and Delete buttons for each job entry.
        """
        edit_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=[obj.pk])
        delete_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete', args=[obj.pk])

        return format_html(
            '<a href="{}" style="margin-right: 5px; padding: 5px 10px; background-color: #007bff; color: white; border-radius: 5px; text-decoration: none;">Edit</a>'
            '<a href="{}" style="padding: 5px 10px; background-color: #dc3545; color: white; border-radius: 5px; text-decoration: none;">Delete</a>',
            edit_url, delete_url
        )

    job_actions.short_description = 'Actions'

    def calculate_average_salary_by_city(self, request, queryset):
        """
        Admin action to calculate the average salary for selected jobs by city.
        """
        city_salaries = {}

        for job in queryset:
            if isinstance(job.salary, (int, float)):  # Ensure salary is numeric
                city_salaries.setdefault(job.location, []).append(job.salary)

        if city_salaries:
            message_lines = ["Average Salaries by City:"]
            for city, salaries in city_salaries.items():
                avg_salary = sum(salaries) / len(salaries)
                message_lines.append(f"{city}: Rs {avg_salary:.2f}")

            self.message_user(request, "\n".join(message_lines), messages.SUCCESS)
        else:
            self.message_user(request, "No valid salaries found in the selection.", messages.WARNING)

    calculate_average_salary_by_city.short_description = "Calculate AVG Salary by City"

    def changelist_view(self, request, extra_context=None):
        """
        Override changelist_view to calculate average salary when searching for a city.
        """
        response = super().changelist_view(request, extra_context)

        search_query = request.GET.get("q", "").strip()  # Get search input
        if search_query:  # If a search is performed
            avg_salary = Job.objects.filter(location__icontains=search_query).aggregate(Avg("salary"))["salary__avg"]
            if avg_salary is not None:
                self.message_user(request, f"Average salary in {search_query}: Rs {avg_salary:.2f}", messages.INFO)

        return response

# Customizing the Django Admin Panel Titles
admin.site.site_header = "Job Portal Admin"
admin.site.site_title = "Job Management"
admin.site.index_title = "Manage Jobs"
