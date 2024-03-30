from django.urls import path
from hospital_management_studio.views import About, Home, Contact, Login, Add_Appoinment, Delete_Appointment , Logout_admin, Index, View_doctor, View_Appointment ,Add_Patient, Delete_Doctor, Add_Doctor, View_Patient, Delete_Patient

urlpatterns = [
    path('about/', About, name='about'),
    path('', Home, name='home'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_doctor, name='view_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('add_apointment/', Add_Appoinment, name='add_appointment'),
    path('delete_doctor/(?P<int:pid>)/', Delete_Doctor, name='delete_doctor'),
    path('delete_patient/(?P<int:pid>)/', Delete_Patient, name='delete_patient'),
    path('delete_appointment/(?P<int:pid>)/', Delete_Appointment, name='delete_appointment'),



]