from django.urls import path
from . import views

urlpatterns = [
    path('LoginForm', views.LoginForm, name = 'LoginForm'),
    path('Logout/', views.Logout, name = 'Logout'),
    path('registration', views.registration, name = 'registration'),

    path('', views.homepage, name = 'homepage'),
    path('patient_view/<str:pk_test>/', views.patient_view, name = 'patient_view'),
    path('doctor_view/<str:pk_test>/', views.doctor_view, name = 'doctor_view'),
    path('inventory_view/', views.inventory_view, name = 'inventory_view'),
    path('patientPage', views.patientPage, name = 'patientPage'),
    path('doctorPage', views.doctorPage, name = 'doctorPage'),

    path('create_patientform/', views.create_patientform, name = 'create_patientform'),
    path('create_doctorform/', views.create_doctorform, name = 'create_doctorform'),
    path('create_inventoryform/', views.create_inventoryform, name = 'create_inventoryform'),
    path('create_billform/', views.create_billform, name = 'create_billform'),
    path('updatepatientbill/<str:pk>/', views.updatepatientbill, name = 'updatepatientbill'),
    path('deletepatientbill/<str:pk>/', views.deletepatientbill, name = 'deletepatientbill'),


    path('updatepatient/<str:pk>/', views.updatepatient, name = 'updatepatient'),
    path('deletepatient/<str:pk>/', views.deletepatient, name = 'deletepatient'),
    path('updatedoctor/<str:pk>/', views.updatedoctor, name = 'updatedoctor'),
    path('deletedoctor/<str:pk>/', views.deletedoctor, name = 'deletedoctor'),
    path('updateinventoryitem/<str:pk>/', views.updateinventoryitem, name = 'updateinventoryitem'),
    path('deleteinventoryitem/<str:pk>/', views.deleteinventoryitem, name = 'deleteinventoryitem'),
]