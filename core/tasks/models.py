from django.db import models
from datetime import datetime
from accounts.models import User



class Task(models.Model):
    
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    is_complete = models.BooleanField(default=False)
    description = models.TextField(null=True)
    start_time = models.DateTimeField(default=datetime.now(), blank=True)
    end_time = models.DateTimeField(blank=True, null=True, )
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
