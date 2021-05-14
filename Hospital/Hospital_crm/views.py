from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .models import *
from .forms import PatientForm, DoctorForm, InventoryForm, RegistrationForm, BillsForm
from .filter import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

# def homepage(request):
#     return HttpResponse("Hello Hospital")
#     # create a general login page for all types of user(Dostors, Admin, Staff, Patient)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception'])
def registration(request):

        form = RegistrationForm()

        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()

        context = {'form':form}

        return render(request, 'registration.html', context)



def LoginForm(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.info(request, 'Username OR Password is incorrect')
        context = {}

        return render(request, 'login.html', context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['reception','admin','patient'])
def patientPage(request):
    
    bill = request.user.patient.bills_set.all()
    print(bill)
    context = {'bill': bill}
	
    return render(request, 'patientPage.html', context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['doctor'])
def doctorPage(request):
	context = {}
	return render(request, 'doctorPage.html', context)


@login_required(login_url='LoginForm')
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/LoginForm')

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception', 'patient'])
def patient_view(request, pk_test):

    pat = Patient.objects.get(id = pk_test)
    bill = Bills.objects.filter(patient = pat)
    context = {'patient': pat, 'bill': bill}
    return render(request, 'patient_view.html', context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception'])
def inventory_view(request):

    inventory = Inventory_item.objects.all()

    myinventoryfilter = InventoryFilterForm(request.GET, queryset=inventory)
    inventory = myinventoryfilter.qs

    context = {'inventory': inventory, 'myinventoryfilter':myinventoryfilter}

    return render(request, 'inventory_view.html', context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception','doctor'])
def doctor_view(request, pk_test):

    appointments = Appointment.objects.all()

    doctor = Doctor.objects.get(id = pk_test)

    if appointments.filter(Doctor = int(pk_test)).exists():
        doc_appointments = appointments.filter(Doctor = int(pk_test)).count()
    else:
        doc_appointments = 0
    context = {'doctor': doctor, 'doc_appointments': doc_appointments}

    return render(request, "doctor_view.html", context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception','patient'])
def create_patientform(request):

    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')


    context = {'form': form}

    return render(request, "create_patientform.html", context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception','doctor'])
def create_billform(request):

    form = BillsForm()
    if request.method == 'POST':
        form = BillsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {'form': form}

    return render(request, "create_patientform.html", context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception','doctor'])
def create_doctorform(request):

    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'form':form}

    return render(request, "create_doctorform.html", context) 

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception'])
def create_inventoryform(request):

    form = InventoryForm()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory_view')
    context = {'form':form}

    return render(request, "create_inventoryform.html", context)    

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception','patient'])
def updatepatient(request, pk):

    patient = Patient.objects.get(id = pk)
    form = PatientForm(instance=patient)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patient_view/{0}/'.format(pk))


    context = {'form': form}

    return render(request, "create_patientform.html", context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception'])
def deletepatient(request, pk):
    patient = Patient.objects.get(id = pk)

    if request.method == 'POST':
        patient.delete()
        return HttpResponseRedirect('/')

    context = {'patient':patient}

    return render(request, "delete_patient.html", context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception'])
def updatepatientbill(request, pk):

    bill = Bills.objects.get(id = pk)
    form = BillsForm(instance=bill)
    
    if request.method == 'POST':
        form = BillsForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')


    context = {'form': form}

    return render(request, "create_billform.html", context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception'])
def deletepatientbill(request, pk):
    bill = Bills.objects.get(id = pk)

    if request.method == 'POST':
        patient.delete()
        return HttpResponseRedirect('/')

    context = {'bill':bill}

    return render(request, "delete_patient.html", context)


@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception','doctor'])
def updatedoctor(request, pk):

    doctor = Doctor.objects.get(id = pk)
    form = DoctorForm(instance=doctor)
    
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/doctor_view/{0}/'.format(pk))


    context = {'form': form}

    return render(request, "create_doctorform.html", context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception'])
def deletedoctor(request, pk):
    doctor = Doctor.objects.get(id = pk)

    if request.method == 'POST':
        doctor.delete()
        return HttpResponseRedirect('/')

    context = {'doctor':doctor}

    return render(request, "delete_doctor.html", context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception'])
def updateinventoryitem(request, pk):

    inventory = Inventory_item.objects.get(id = pk)
    form = InventoryForm(instance=inventory)
    
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory_view/')


    context = {'form': form}

    return render(request, "create_inventoryform.html", context)

@login_required(login_url='LoginForm')
@allowed_users(allowed_roles = ['admin', 'reception'])
def deleteinventoryitem(request, pk):
    
    inventory = Inventory_item.objects.get(id = pk)

    if request.method == 'POST':
        inventory.delete()
        return HttpResponseRedirect('/inventory_view')

    context = {'inventory':inventory}

    return render(request, "delete_inventoryitem.html", context)


@login_required(login_url='LoginForm')
@admin_only
def homepage(request):

    patient = Patient.objects.all()
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.all()

    inpatient = patient.filter(Patient_Type = 'Inpatient').count()
    appointments_pending = appointments.filter(Status='Pending').count()
    appointments_approved = appointments.filter(Status='Approved').count()

    params = {'doctors' : doctors, 'patient' : patient, 'inpatient':inpatient, 'appointments_pending':appointments_pending, 'appointments_approved':appointments_approved}
    
    return render(request, 'homepage.html', params)