from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, MedicalRecord

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', \
            'gender', 'birthday', 'mobile', 'address', 'emergency_contact', 'emergency_number']

class PatientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    gender = forms.CharField()
    birthday = forms.DateField()
    mobile = forms.CharField()
    address = forms.CharField()
    emergency_contact = forms.CharField()
    emergency_number = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', \
            'gender', 'birthday', 'mobile', 'address', 'emergency_contact', 'emergency_number']
    def save(self, commit=True):
        user = super(PatientRegistrationForm, self).save(False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = user.email
        user.save()
        profile = user.profile
        profile.email = self.cleaned_data['email']
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.gender = self.cleaned_data['gender']
        profile.birthday = self.cleaned_data['birthday']
        profile.mobile = self.cleaned_data['mobile']
        profile.address = self.cleaned_data['address']
        profile.emergency_contact = self.cleaned_data['emergency_contact']
        profile.emergency_number = self.cleaned_data['emergency_number']
        profile.is_patient = True
        if commit:
            user.save()
            profile.save()
        return user

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', \
            'gender', 'mobile', 'address']  # 'birthday',

class DoctorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    gender = forms.CharField()
    # birthday = forms.DateField()
    mobile = forms.CharField()
    address = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', \
            'gender', 'mobile', 'address']  # 'birthday', 
    def save(self, commit=True):
        user = super(DoctorRegistrationForm, self).save(False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = user.email
        user.save()
        profile = user.profile
        profile.email = self.cleaned_data['email']
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.gender = self.cleaned_data['gender']
        # profile.birthday = self.cleaned_data['birthday']
        profile.mobile = self.cleaned_data['mobile']
        profile.address = self.cleaned_data['address']
        profile.is_doctor = True
        if commit:
            user.save()
            profile.save()
        return user

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['brief', 'diagnosis', 'prescription', 'doctor', 'date']
    def save(self, patient, user, commit=True):
        rec = super(MedicalRecordForm, self).save(False)
        if rec.patient_id == 0:
            rec.patient_id = patient.id
            rec.created_by_id = user.id
        elif rec.patient_id != patient.id:
            raise 'mismatch'
        rec.updated_by_id = user.id
        if commit:
            rec.save()
        return rec

# class RecordListForm(forms.Form):
#     patient = forms.CharField(max_length=50)

class SetPatientForm(forms.Form):
    patient = forms.CharField(max_length=50)
