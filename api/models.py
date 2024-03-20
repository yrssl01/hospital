from django.db import models

# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    experience = models.PositiveIntegerField()
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    
    @property
    def full_name(self):
        return '%s %s'%(self.first_name, self.last_name)
    

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    
    @property
    def full_name(self):
        return '%s %s'%(self.first_name, self.last_name)
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    PLANNED = 'PLANNED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (PLANNED, PLANNED),
        (COMPLETED, COMPLETED),
        (CANCELLED, CANCELLED)
    ]
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.doctor.full_name} | {self.patient.full_name} | {self.appointment_time}"

    



