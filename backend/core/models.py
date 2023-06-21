from django.db import models
from accounts.models import User
import uuid

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-").lower()
        super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/doctors/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-").lower()
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    


class Apointment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE,  blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,  blank=True, null=True)
    name = models.CharField(max_length=50)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_no = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name + " - " + self.doctor.name + " - " + str(self.date) + " - " + str(self.time)

