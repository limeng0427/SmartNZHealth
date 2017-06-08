from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    active = models.BooleanField(default=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_doctor_emergency = models.BooleanField(default=False)
    # use local email, first_name, last_name
    email = models.EmailField(blank=False, default='x')
    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, blank=False, default='')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    birthday = models.DateField(default=timezone.now)
    # https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(max_length=16, validators=[phone_regex],
                              blank=False, default='0000000000')
    # validators should be a list
    address = models.CharField(max_length=250, blank=True)
    emergency_contact = models.CharField(max_length=100, default='')
    emergency_number = models.CharField(max_length=16, validators=[phone_regex],
                                        blank=False, default='0000000000')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def find_user(id):
    user = User.objects.filter(id=id)
    return user[0] if user.count() > 0 else None

def username_or_none(id):
    user = find_user(id)
    return user.username if user else ''

class MedicalRecord(models.Model):
    patient_id = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by_id = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_by_id = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    inactive_by_id = models.PositiveIntegerField(default=0)
    brief = models.CharField(max_length=200)
    diagnosis = models.TextField()
    prescription = models.TextField()
    doctor = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)

    created_by = property(lambda x: username_or_none(x.created_by_id))
    updated_by = property(lambda x: username_or_none(x.updated_by_id))

def record_briefd_or_none(id):
    rec = MedicalRecord.objects.filter(id=id)
    return rec[0].brief if rec.count() > 0 else None
    
class VisitRecord(models.Model):
    visitor_id = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    visit_type = models.CharField(max_length=50, default='list')
    # 'create', list', 'detail', 'update', 'delete'
    record_id = models.PositiveIntegerField(default=0) # MedicalRecord.id
    patient_id = models.PositiveIntegerField(default=0) # MedicalRecord.patient_id

    visitor = property(lambda x: username_or_none(x.visitor_id))
    patient = property(lambda x: username_or_none(x.patient_id))
    record_brief = property(lambda x: record_brief_or_none(x.record_id))
