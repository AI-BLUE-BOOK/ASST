from djongo import models

class Job(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    position_name = models.CharField(max_length=255,db_column="positionName")
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)  # Changed to IntegerField
    rating = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "python_jobs"  

    def __str__(self):
        return self.position_name
