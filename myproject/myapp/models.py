from django.db import models

class HealthRecord(models.Model):
    user_name = models.CharField(max_length=100)
    heart_rate = models.IntegerField()
    blood_pressure = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.created_at}"


    

