from django.db import models
from django.core.exceptions import ValidationError
from phone_field import PhoneField
from django.contrib.auth.models import User


# Create your models here.

class Patient(models.Model):

    genderchoices = (
        ('male', 'Male'),
        ('female','Female'),
        ('other','Other')
    )

    patientchoices = (
        ('Inpatient', 'Inpatient'),
        ('Outpatient', 'Outpatient')
    )

    user = models.OneToOneField(User,null=True, on_delete = models.CASCADE)
    Patient_Type = models.CharField(max_length=10, choices=patientchoices, default='Inpatient')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null = True)
    Mobile_number = PhoneField(blank=False)
    Address = models.CharField(max_length=200, null = True)
    gender = models.CharField(max_length=10, default='Male', choices=genderchoices)

    def __str__(self):
        return self.name

class Receptionist(models.Model):

    genderchoices = (('male', 'Male'),('female','Female'),('other','Other'))

    user = models.OneToOneField(User,null=True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null = True)
    Mobile_number = PhoneField(blank=False)
    Address = models.CharField(max_length=200, null = True)
    gender = models.CharField(max_length=10, default='Male', choices=genderchoices)

    def __str__(self):
        return self.name

class Doctor(models.Model):

    genderchoices = (
        ('male', 'Male'),
        ('female','Female'),
        ('other','Other')
    )

    user = models.OneToOneField(User,null=True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null = True)
    Mobile_number = PhoneField(blank=False)
    Address = models.CharField(max_length=200, null = True)
    gender = models.CharField(max_length=10, default='Male', choices=genderchoices)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'rejected'),
        ('Completed', 'Completed'),
    )

    Patient = models.ForeignKey(Patient, null = True, on_delete = models.CASCADE)
    Doctor = models.ForeignKey(Doctor, null = True, on_delete = models.CASCADE)
    Date = models.DateTimeField(null=True)
    Status = models.CharField(max_length=15, null = True, choices=STATUS, default='Pending')

    def __str__(self):
        return "{0} - {1}".format(self.Patient, self.Doctor)

class Inventory_item(models.Model):

    categorychoices = (
        ('Essential', 'Essential'),
        ('Sanitization', 'Sanitization')
    )
    item = models.TextField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=50, choices=categorychoices, null=True)
    supplier = models.CharField(max_length=50, null=True)
    supplier_contact = PhoneField(null = True)

    def __str__(self):
        return "{0} - {1}".format(self.item, self.quantity)

class Bills(models.Model):

    billchoices = (
        ('Lab Test','Lab Test'),
        ('Room Charges','Room Charges'),
        ('Doctor Visits','Doctor Visits'),
        ('Lunch','Lunch'),
        ('Medicines', 'Medicines'),
        ('First Visit', 'First Visit'),
        ('Followup Visit', 'Followup Visit'),
        ('In Comments', 'In Comments')
    )
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    Date = models.DateField()
    amount = models.IntegerField(null=True)
    type = models.CharField(max_length=200, choices=billchoices)
    Comments = models.TextField(max_length=500, null=True)

    def __str__(self):
        return "{0} - {1}".format(self.patient, self.type)