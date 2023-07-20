from typing import Any
from django import forms
# from django.forms.fields import Field
from .models import Task, Category
# from datetime import datetime
# from subtasks.models import SubTask




class TaskForm(forms.ModelForm):
    # add_subtask = forms.CharField(max_length=255, required=False)
    # start_time = forms.DateInput()
    class Meta:
        model = Task
        fields = ['title', 'category', 'start_time', 'end_time']
    
    
class DetailForm(forms.ModelForm):
    # subtask=forms.CharField(max_length=255, required=False)
    # category = forms.CharField()
    class Meta:
        model = Task
        fields = ['title', 'category', 'description','is_complete', 'start_time', 'end_time']
    