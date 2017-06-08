from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import Http404

# Create your views here.
@login_required
def user_profile(request):
    if request.method == 'GET':
        if request.user.profile.is_patient:
            form = PatientProfileForm(instance=request.user.profile)
        else:
            form = DoctorProfileForm(instance=request.user.profile)
    else:
        if request.user.profile.is_patient:
            form = PatientProfileForm(data=request.POST, instance=request.user.profile)
        else:
            form = DoctorProfileForm(data=request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'profile.html', {'form':form})

def home(request):
    # get groups for test
    return render(request, 'home.html', {'title':"Home Page"})

def forgot_password(request):
    # get groups for test
    return render(request, 'home.html', {'title':"forgot_password"})

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        for g in user.groups.all():
            print(g, type(g))
        return redirect('/')
    return render(request, 'login.html', {'error':'invalid username or password'})

@login_required(login_url='/userprofile/login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')

def register_patient(request):
    if request.method == 'GET':
        return render(request, 'register_patient.html', {'form':PatientRegistrationForm()})
    form = PatientRegistrationForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        auth.login(request, user)
        return redirect('/')
    return render(request, 'register_patient.html', {'form':form})

def register_doctor(request):
    if request.method == 'GET':
        return render(request, 'register_doctor.html', {'form':DoctorRegistrationForm()})
    form = DoctorRegistrationForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        auth.login(request, user)
        return redirect('/')
    return render(request, 'register_doctor.html', {'form':form})

# https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html
@login_required(login_url='/userprofile/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # important
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form':form})

def doctor_get_patient_in_session(request):
    if not request.user.profile.is_doctor:
        return None
    if 'patient' not in request.session:
        return None
    patient = get_object_or_404(User, username=request.session['patient'])
    if not patient.profile.is_patient:
        raise Http404
    # security check
    return patient

@login_required
def rec_create(request):
    patient = doctor_get_patient_in_session(request)
    if patient is None:
        return redirect('/')
    if request.method == 'GET':
        form = MedicalRecordForm()
        return render(request, 'record_create.html', {'form':form, 'submit':'Create'})
    else:
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            rec = form.save(patient=patient, user=request.user, commit=True)
            print('rec_create', type(rec))
            print(rec.id, rec.patient_id, rec.created_by_id)
            # create visit record
            visit = VisitRecord.objects.create(visitor_id=request.user.id,
                                               visit_type='create',
                                               record_id=rec.id,
                                               patient_id=patient.id)
            return render(request, 'record_detail.html', {'rec':rec, 'patient':patient})
    return redirect('/')

@login_required
def rec_detail(request, rec_id):
    rec = get_object_or_404(MedicalRecord, id=rec_id)
    patient = get_object_or_404(User, id=rec.patient_id)
    return render(request, 'record_detail.html', {'rec':rec, 'patient':patient})
    pass

@login_required(login_url='/userprofile/login')
def rec_list(request):
    if request.user.profile.is_patient: # patient can list his own records
        data = MedicalRecord.objects.filter(patient_id=request.user.id)
        return render(request, 'record_list.html', {'data':data, 'patient':request.user})
    patient = doctor_get_patient_in_session(request)
    if patient is None:
        return redirect('/')
    data = MedicalRecord.objects.filter(patient_id=patient.id)
    return render(request, 'record_list.html', {'data':data, 'patient':patient})

@login_required
def rec_update(request):
    pass

@login_required
def rec_delete(request):
    pass

@login_required
def set_patient(request):
    if request.method == 'GET':
        return render(request, 'form.html', {'form':SetPatientForm(), 'submit':'Set'})
    else:
        form = SetPatientForm(request.POST)
        if form.is_valid():
            #print('patient=', form.cleaned_data['patient'], type(form.cleaned_data['patient']))
            patient = get_object_or_404(User, username=form.cleaned_data['patient'])
            if not patient.profile.is_patient:
                raise Http404
            request.session['patient'] = patient.username
        return redirect('/')

@login_required
def visit_list(request):
    if request.user.profile.is_patient: # patient can list his own records
        data = VisitRecord.objects.filter(patient_id=request.user.id)
        return render(request, 'visit_list.html', {'data':data})
    if request.user.profile.is_doctor: # patient can list his own records
        data = VisitRecord.objects.filter(visitor_id=request.user.id)
        return render(request, 'visit_list.html', {'data':data})
    return redirect('/')

