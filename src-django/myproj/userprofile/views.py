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
from django.db.models import Q


# Create your views here.
@login_required(login_url='/userprofile/login')
def user_profile(request):
    if request.user.profile.is_patient:
        form = PatientProfileForm(request.POST or None, instance=request.user.profile)
    elif request.user.profile.is_doctor:
        form = DoctorProfileForm(request.POST or None, instance=request.user.profile)
    else:
        return redirect('/')
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'profile.html', {'form':form, 'title':'Profile'})

def home(request):
    # get groups for test
    return render(request, 'home.html', {'title':"Home Page"})

def contact(request):
    # get groups for test
    return render(request, 'contact.html', {'title':"Contact"})

@login_required(login_url='/userprofile/login')
def forgot_password(request):
    # get groups for test
    return render(request, 'home.html', {'title':"Reset Password"})

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # for g in user.groups.all():
            #     print(g, type(g))
            return redirect('/')
        messages.error(request, 'Invalid username or password')
    return render(request, 'login.html', {'title':"Login"})

@login_required(login_url='/userprofile/login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')

def register_patient(request):
    form = PatientRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        if user:
            auth.login(request, user)
            return redirect('/')
        messages.error(request, 'duplicate username')
    return render(request, 'register_patient.html', {'form':form, 'title':"Register Patient"})

def register_doctor(request):
    form = DoctorRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        if user:
            auth.login(request, user)
            return redirect('/')
        messages.error(request, 'duplicate username')
    return render(request, 'register_doctor.html', {'form':form, 'title':"Register Doctor"})

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
    return render(request, 'change_password.html', {'form':form, 'title':'Change Password'})

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

@login_required(login_url='/userprofile/login')
def rec_create(request):
    patient = doctor_get_patient_in_session(request)
    if patient is None:
        return redirect('/')
    if request.method == 'GET':
        form = MedicalRecordForm()
        return render(request, 'record_create.html', {'form':form, 'submit':'Create', 'title':"Create Record"})
    else:
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            rec = form.save(patient=patient, user=request.user, commit=True)
            print('rec_create', type(rec))
            print(rec.id, rec.patient_id, rec.created_by_id)
            # create visit record
            VisitRecord.objects.create(visitor_id=request.user.id,
                                       visit_type='create',
                                       record_id=rec.id,
                                       patient_id=patient.id)
            return render(request, 'record_detail.html', {'rec':rec, 'patient':patient, 'title':"Create Record"})
    return redirect('/')

@login_required(login_url='/userprofile/login')
def rec_detail(request, rec_id):
    rec = get_object_or_404(MedicalRecord, id=rec_id)
    patient = get_object_or_404(User, id=rec.patient_id)
    if request.user.profile.is_doctor:
        VisitRecord.objects.create(visitor_id=request.user.id,
                                   visit_type='detail',
                                   record_id=rec.id,
                                   patient_id=patient.id)
    return render(request, 'record_detail.html', {'rec':rec, 'patient':patient, 'title':"Record Detail"})

@login_required(login_url='/userprofile/login')
def rec_list(request):
    if request.user.profile.is_patient: # patient can list his own records
        data = MedicalRecord.objects.filter(patient_id=request.user.id)
        patient = request.user
    else:
        patient = doctor_get_patient_in_session(request)
        if patient is None:
            return redirect('/')
        data = MedicalRecord.objects.filter(patient_id=patient.id)
    search = request.GET.get('search')
    if search and len(search) > 0:
        data = data.filter(
            Q(brief__icontains=search)|
            Q(diagnosis__icontains=search)|
            Q(prescription__icontains=search)
            ).distinct()
    if request.user.profile.is_doctor:
        for rec in data:
            VisitRecord.objects.create(visitor_id=request.user.id,
                                    visit_type='list',
                                    record_id=rec.id,
                                    patient_id=patient.id)
    return render(request, 'record_list.html', {'data':data, 'patient':patient, 'title':"List Records"})

@login_required(login_url='/userprofile/login')
def rec_update(request):
    pass

@login_required(login_url='/userprofile/login')
def rec_delete(request):
    pass

@login_required(login_url='/userprofile/login')
def set_patient(request):
    form = SetPatientForm(request.POST or None)
    if form.is_valid():
        #print('patient=', form.cleaned_data['patient'], type(form.cleaned_data['patient']))
        patient = get_object_or_404(User, username=form.cleaned_data['patient'])
        if not patient.profile.is_patient:
            raise Http404
        request.session['patient'] = patient.username
        return redirect('/')
    return render(request, 'set_patient.html', {'form':form, 'submit':'Set', 'title':'Set Patient'})

@login_required(login_url='/userprofile/login')
def visit_list(request):
    if request.user.profile.is_patient: # patient can list his own records
        data = VisitRecord.objects.filter(patient_id=request.user.id)
    elif request.user.profile.is_doctor: # patient can list his own records
        data = VisitRecord.objects.filter(visitor_id=request.user.id)
    else:
        return redirect('/')
    data = data.order_by('-timestamp')
    return render(request, 'visit_list.html', {'data':data, 'title':"List Visit History"})

