from django.contrib import admin
from .models import Department, Doctor, Apointment
# Register your models here.


@admin.register(Apointment)
class ApointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor', 'date', 'time', 'email', 'phone_no', 'message', 'uuid')
    list_filter = ('doctor', 'date', 'time')
    search_fields = ('name', 'doctor__name', 'date', 'time', 'email', 'phone_no', 'message', 'uuid')
    readonly_fields = ('uuid',)
    ordering = ('-date', '-time')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    readonly_fields = ('slug',)
    ordering = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'description', 'image', 'slug')
    list_filter = ('name', 'department', 'slug')
    search_fields = ('name', 'department__name', 'slug')
    readonly_fields = ('slug',)
    ordering = ('name',)


