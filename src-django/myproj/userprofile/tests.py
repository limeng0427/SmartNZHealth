from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import *
from .forms import *

# Create your tests here.
class LoginTest(TestCase):
    username = 'temporary@host.tld'
    password = 'temporary'
    passbad  = 'asdf'
    email = username
    def setUp(self):
        user = User.objects.create_user(self.username, email=self.email, password=self.password)
 
    def test_login_ok(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/', follow=True)
        user = User.objects.get(username=self.username)
        self.assertEqual(response.context['user'].username, self.username)

    def test_login_fail(self):  # fail for password not match
        self.client.login(username=self.username, password=self.passbad)
        response = self.client.get('/', follow=True)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        self.client.logout()
        response = self.client.get('/', follow=True)
        self.assertFalse(response.context['user'].is_authenticated)

class PatientRegistrationFormTest(TestCase):
    username = 'testregister@host.tld'
    password = 'temporary'
    passbad  = 'asdf'
    email = username
    first_name = 'first name'
    last_name = 'last_name'
    gender = 'M'
    birthday = '2000-01-02'
    mobile = '1234567890'
    address = 'asfd123puqwpeor097z09xcv'
    emergency_contact = 'John Doe'
    emergency_number = '1234567890'
    def test_register_ok(self):
        form_data = {'username': self.username, 'password1':self.password, 'password2':self.password, 'email':self.email,
                     'first_name': self.first_name, 'last_name':self.last_name, 'gender':self.gender, 'birthday':self.birthday,
                     'mobile':self.mobile, 'address':self.address, 'emergency_contact':self.emergency_contact, 'emergency_number':self.emergency_number}
        form = PatientRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_fail(self):   # fail for password not match
        form_data = {'username': self.username, 'password1':self.password, 'password2':self.passbad, 'email':self.email,
                     'first_name': self.first_name, 'last_name':self.last_name, 'gender':self.gender, 'birthday':self.birthday,
                     'mobile':self.mobile, 'address':self.address, 'emergency_contact':self.emergency_contact, 'emergency_number':self.emergency_number}
        form = PatientRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

class DoctorRegistrationFormTest(TestCase):
    username = 'testregister@host.tld'
    password = 'temporary'
    passbad  = 'asdf'
    email = username
    first_name = 'first name'
    last_name = 'last_name'
    gender = 'M'
    mobile = '1234567890'
    address = 'asfd123puqwpeor097z09xcv'
    def test_register_ok(self):
        form_data = {'username': self.username, 'password1':self.password, 'password2':self.password, 'email':self.email,
                     'first_name': self.first_name, 'last_name':self.last_name, 'gender':self.gender, 
                     'mobile':self.mobile, 'address':self.address,}
        form = DoctorRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_fail(self):   # fail for password not match
        form_data = {'username': self.username, 'password1':self.password, 'password2':self.passbad, 'email':self.email,
                     'first_name': self.first_name, 'last_name':self.last_name, 'gender':self.gender, 
                     'mobile':self.mobile, 'address':self.address,}
        form = DoctorRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
    
class RegisterPatientTest(TestCase):
    url = reverse("userprofile:register_patient")
    username = 'testregister@host.tld'
    password = 'temporary'
    passbad  = 'asdf'
    email = username
    first_name = 'first name'
    last_name = 'last_name'
    gender = 'M'
    birthday = '2000-01-02'
    mobile = '1234567890'
    address = 'asfd123puqwpeor097z09xcv'
    emergency_contact = 'John Doe'
    emergency_number = '1234567890'

    def test_register_fail_wrongpass(self): # fail for password not match
        form_data = {'username': self.username, 'password1':self.password, 'password2':self.passbad, 'email':self.email,
                     'first_name': self.first_name, 'last_name':self.last_name, 'gender':self.gender, 'birthday':self.birthday,
                     'mobile':self.mobile, 'address':self.address, 'emergency_contact':self.emergency_contact, 'emergency_number':self.emergency_number}
        response = self.client.post(self.url, form_data, follow=True)
        user = response.context['user']
        self.assertFalse(user.is_authenticated)

    def test_register_ok(self):
        form_data = {'username': self.username, 'password1':self.password, 'password2':self.password, 'email':self.email,
                     'first_name': self.first_name, 'last_name':self.last_name, 'gender':self.gender, 'birthday':self.birthday,
                     'mobile':self.mobile, 'address':self.address, 'emergency_contact':self.emergency_contact, 'emergency_number':self.emergency_number}
        response = self.client.post(self.url, form_data, follow=True)
        user = response.context['user']
        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.profile.is_patient)
        self.assertEqual(user.username, self.username)
        user = User.objects.get(username=self.username)
        self.assertEqual(user.username, self.username)

    def test_register_fail_dupname(self):   # fail for duplicate name
        self.test_register_ok()
        self.client.logout()
        form_data = {'username': self.username, 'password1':self.password, 'password2':self.password, 'email':self.email,
                     'first_name': self.first_name, 'last_name':self.last_name, 'gender':self.gender, 'birthday':self.birthday,
                     'mobile':self.mobile, 'address':self.address, 'emergency_contact':self.emergency_contact, 'emergency_number':self.emergency_number}
        response = self.client.post(self.url, form_data, follow=True)
        user = response.context['user']
        self.assertFalse(user.is_authenticated)


# class UserProfileTest(TestCase):
#     username = 'testregister@host.tld'
#     password = 'temporary'
#     passbad  = 'asdf'
#     email = username
#     first_name = 'first name'
#     last_name = 'last_name'
#     gender = 'M'
#     birthday = '2000-01-02'
#     mobile = '1234567890'
#     address = 'asfd123puqwpeor097z09xcv'
#     emergency_contact = 'John Doe'
#     emergency_number = '1234567890'
#     def test_update(self):
#         # create a user
#         user = User.objects.create_user(self.username, password=self.password)
#         self.client.login(username=self.username, password=self.password)
#         form_data = {'attr1':True, 'attr2':'bbb'}
#         response = self.client.post(reverse('userprofile:profile'), form_data, follow=True)
#         profile = user.profile
#         self.assertEqual(profile.attr1, form_data['attr1'])
#         self.assertEqual(profile.attr2, form_data['attr2'])
