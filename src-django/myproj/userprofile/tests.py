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
    url = reverse("userprofile:login")
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

    def test_login_post(self):
        data = {'username':self.username, 'password':self.password}
        response = self.client.post(self.url, data, follow=True)
        user = response.context['user']
        self.assertTrue(user.is_authenticated)

    def test_login_post_fail(self):
        data = {'username':self.username, 'password':self.passbad}
        response = self.client.post(self.url, data, follow=True)
        user = response.context['user']
        self.assertFalse(user.is_authenticated)
        self.assertTrue(response.content.find(b'Invalid username or password') >= 0)

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
    data = {'password1':password, 'password2':password,
            'email':email, 'first_name': first_name, 'last_name':last_name, 
            'gender':gender, 'birthday':birthday, 'mobile':mobile,
            'address':address, 'emergency_contact':emergency_contact,
            'emergency_number':emergency_number}
    def test_register_ok(self):
        form_data = self.data
        form = PatientRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_fail(self):   # fail for password not match
        form_data = self.data.copy()
        form_data['password2'] = self.passbad
        form = PatientRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

class DoctorRegistrationFormTest(TestCase):
    username = 'testregister@host.tld'
    password = 'temporary'
    passbad = 'asdf'
    email = username
    first_name = 'first name'
    last_name = 'last_name'
    gender = 'M'
    mobile = '1234567890'
    address = 'asfd123puqwpeor097z09xcv'
    data = {'password1':password, 'password2':password, 'email':email,
            'first_name':first_name, 'last_name':last_name, 'gender':gender, 
            'mobile':mobile, 'address':address,}
    def test_register_ok(self):
        form_data = self.data
        form = DoctorRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_fail(self):   # fail for password not match
        form_data = self.data.copy()
        form_data['password2'] = self.passbad
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
    data = {'password1':password, 'password2':password,
            'email':email, 'first_name': first_name, 'last_name':last_name, 
            'gender':gender, 'birthday':birthday, 'mobile':mobile,
            'address':address, 'emergency_contact':emergency_contact,
            'emergency_number':emergency_number}
    def test_register_fail_wrongpass(self): # fail for password not match
        form_data = self.data.copy()
        form_data['password2'] = self.passbad
        response = self.client.post(self.url, form_data, follow=True)
        self.assertTrue(response.content.find(b"password fields didn&#39;t match.") >= 0)
        user = response.context['user']
        self.assertFalse(user.is_authenticated)

    def test_register_ok(self):
        form_data = self.data
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
        form_data = self.data
        response = self.client.post(self.url, form_data, follow=True)
        user = response.context['user']
        self.assertFalse(user.is_authenticated)
        self.assertTrue(response.content.find(b"duplicate username") >= 0)

    def test_register_miss_field(self):
        for k in self.data:
            form_data = self.data.copy()
            del form_data[k]
            response = self.client.post(self.url, form_data, follow=True)
            user = response.context['user']
            self.assertFalse(user.is_authenticated)
            self.assertTrue(response.content.find(b"This field is required") >= 0)

class RegisterDoctorTest(TestCase):
    url = reverse("userprofile:register_doctor")
    username = 'testregister@host.tld'
    password = 'temporary'
    passbad = 'asdf'
    email = username
    first_name = 'first name'
    last_name = 'last_name'
    gender = 'M'
    mobile = '1234567890'
    address = 'asfd123puqwpeor097z09xcv'
    data = {'password1':password, 'password2':password, 'email':email,
            'first_name':first_name, 'last_name':last_name, 'gender':gender, 
            'mobile':mobile, 'address':address,}
    def test_register_fail_wrongpass(self): # fail for password not match
        form_data = self.data.copy()
        form_data['password2'] = self.passbad
        response = self.client.post(self.url, form_data, follow=True)
        self.assertTrue(response.content.find(b"password fields didn&#39;t match.") >= 0)
        user = response.context['user']
        self.assertFalse(user.is_authenticated)

    def test_register_ok(self):
        form_data = self.data
        response = self.client.post(self.url, form_data, follow=True)
        user = response.context['user']
        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.profile.is_doctor)
        self.assertEqual(user.username, self.username)
        user_db = User.objects.get(username=self.username)
        self.assertEqual(user.id, user_db.id)

    def test_register_fail_dupname(self):   # fail for duplicate name
        self.test_register_ok()
        self.client.logout()
        form_data = self.data
        response = self.client.post(self.url, form_data, follow=True)
        user = response.context['user']
        self.assertFalse(user.is_authenticated)
        self.assertTrue(response.content.find(b"duplicate username") >= 0)

    def test_register_miss_field(self):
        for k in self.data:
            form_data = self.data.copy()
            del form_data[k]
            response = self.client.post(self.url, form_data, follow=True)
            user = response.context['user']
            self.assertFalse(user.is_authenticated)
            self.assertTrue(response.content.find(b"This field is required") >= 0)

class PatientProfileFormTest(TestCase):
    # ['first_name', 'last_name', \
    #         'gender', 'birthday', 'mobile', 'address', 'emergency_contact', 'emergency_number']
    url = reverse('userprofile:profile')
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
    data = {'password1':password, 'password2':password,
            'email':email, 'first_name': first_name, 'last_name':last_name, 
            'gender':gender, 'birthday':birthday, 'mobile':mobile,
            'address':address, 'emergency_contact':emergency_contact,
            'emergency_number':emergency_number}
    def setUp(self):
        form_data = self.data
        response = self.client.post(reverse("userprofile:register_patient"),
                                    form_data, follow=True)
        user = response.context['user']
        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.profile.is_patient)
        self.assertEqual(user.username, self.username)

    def test_form(self):
        form = PatientProfileForm(self.data)
        self.assertTrue(form.is_valid())

    def test_update(self):
        address2 = 'new address'
        form_data = self.data.copy()
        form_data['address'] = address2
        response = self.client.post(self.url, form_data, follow=True)
        user = User.objects.get(username=self.username)
        self.assertTrue(user.profile.is_patient)
        self.assertEqual(user.profile.address, address2)

class DoctorProfileFormTest(TestCase):
    # ['first_name', 'last_name', \
    #         'gender', 'mobile', 'address']  # 'birthday',
    url = reverse('userprofile:profile')
    username = 'testregister@host.tld'
    password = 'temporary'
    passbad = 'asdf'
    email = username
    first_name = 'first name'
    last_name = 'last_name'
    gender = 'M'
    mobile = '1234567890'
    address = 'asfd123puqwpeor097z09xcv'
    data = {'password1':password, 'password2':password, 'email':email,
            'first_name':first_name, 'last_name':last_name, 'gender':gender, 
            'mobile':mobile, 'address':address,}
    def setUp(self):
        form_data = self.data
        response = self.client.post(reverse("userprofile:register_doctor"),
                                    form_data, follow=True)
        user = response.context['user']
        self.assertTrue(user.is_authenticated)
        self.assertTrue(user.profile.is_doctor)
        self.assertEqual(user.username, self.username)

    def test_form(self):
        form = DoctorProfileForm(self.data)
        self.assertTrue(form.is_valid())

    def test_update(self):
        address2 = 'new address'
        form_data = self.data.copy()
        form_data['address'] = address2
        response = self.client.post(self.url, form_data, follow=True)
        user = User.objects.get(username=self.username)
        self.assertTrue(user.profile.is_doctor)
        self.assertEqual(user.profile.address, address2)

