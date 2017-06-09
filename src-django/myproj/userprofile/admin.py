from django.contrib import admin
from .models import UserProfile, MedicalRecord, VisitRecord
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'id'] # email', 'first_name', 'last_name']
    # list_filter = ('is_staff', 'is_superuser')
    pass
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'is_patient', 'is_doctor' ]
    # list_display = ['title', 'updated',  'timestamp']
    # list_display_links = ['updated']  # set which column to display link
    # list_editable = ['title']  # edit title in the list
    # search_fields = ['title', 'content']  # enables search box
    class Meta:
        model = UserProfile
admin.site.register(UserProfile, UserProfileModelAdmin)

class MedicalRecordModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient_id']
    # list_display = ['title', 'updated',  'timestamp']
    # list_display_links = ['updated']  # set which column to display link
    # list_editable = ['title']  # edit title in the list
    # search_fields = ['title', 'content']  # enables search box
    class Meta:
        model = MedicalRecord
admin.site.register(MedicalRecord, MedicalRecordModelAdmin)

class VisitRecordModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'visitor_id', 'timestamp', 'visit_type', 'record_id', 'patient_id']
    # list_display_links = ['updated']  # set which column to display link
    # list_editable = ['title']  # edit title in the list
    # search_fields = ['title', 'content']  # enables search box
    class Meta:
        model = VisitRecord
admin.site.register(VisitRecord, VisitRecordModelAdmin)
