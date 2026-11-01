from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    emil = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add= True) #set Once
    updated_at = models.DateTimeField(auto_now= True) #update on every change

    def __str__(self):
        return f"{self.name} ({self.email})"
