from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    consulting_date = models.DateField()
    doctor_name = models.CharField(max_length=100)
    diagnosis = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return self.name