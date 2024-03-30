from django.db import models

# Create your models here.

class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Patient(models.Model):
    Name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    mobile = models.IntegerField(null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.Name

class Appoinment(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.Doctor.Name + " " + self.Patient.Name