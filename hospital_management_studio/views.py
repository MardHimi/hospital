from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from hospital_management_studio.models import Doctor, Patient, Appoinment
from django.shortcuts import get_object_or_404, redirect
from .models import Doctor

# Create your views here.

def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('Login')

    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appoinment.objects.all()
    d=0
    p=0
    a=0
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1

    d1={'d':d, 'p':p,'a':a}

    return render(request, 'index.html', d1)

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"

            else:
                error = "yes"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'Login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('Login')
    logout(request)
    return redirect('admin_login')

def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc' : doc}
    return render(request, 'view_doctor.html', d)

def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['Name']
        m = request.POST['mobile']
        sp = request.POST['special']

        try:
            Doctor.objects.create(Name=n, mobile=m, special=sp)
            error = 'no'

        except:
            error = 'yes'

    d = {'error': error}
    return render(request, 'add_doctor.html', d)


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc' : doc}
    return render(request, 'view_patient.html', d)

def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['Name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']

        try:
            Patient.objects.create(Name=n, gender=g, mobile=m, address=a)
            error = 'no'

        except:
            error = 'yes'

    d = {'error': error}
    return render(request, 'add_patient.html', d)


def Add_Appoinment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == 'POST':
        n = request.POST['doctor']
        p = request.POST['patient']
        da = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(Name=n).first()
        patient = Patient.objects.filter(Name=p).first()

        try:
            Appoinment.objects.create(Doctor=doctor, Patient=patient, date=da, time=t)
            error = 'no'

        except:
            error = 'yes'

    d = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'add_appointment.html', d)

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Appoinment.objects.all()
    d = {'doc' : doc}
    return render(request, 'view_appointment.html', d)

def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    app = Appoinment.objects.get(id=pid)
    app.delete()
    return redirect('view_appointment')

