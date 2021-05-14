from django.forms import ModelForm
from .models import Patient, Doctor, Inventory_item, Bills
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class PatientForm(ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'

class DoctorForm(ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'

class InventoryForm(ModelForm):

    class Meta:
        model = Inventory_item
        fields = '__all__'

class BillsForm(ModelForm):

    class Meta:
        model = Bills
        fields = '__all__'
