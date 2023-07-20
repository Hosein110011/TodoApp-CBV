from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Task, Category
from .forms import TaskForm, DetailForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView
import ast
from django.http import Http404
from  django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin 




class HomeView(LoginRequiredMixin,View):
    form_class = TaskForm
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user)
        tasks = tasks.order_by('-created_time')        
        initial = {"key":"value"}
        form = self.form_class(initial=initial)
        return render(request ,'home.html' , {'form':form, 'tasks':tasks})
    
    def post(self, request):
        tasks = Task.objects.filter(user=request.user)
        tasks = tasks.order_by('-created_time')
        form = TaskForm(self.request.POST)
        if form.is_valid():
            user = self.request.user
            title = request.POST['title']
            category = request.POST['category']
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']
            if (end_time!=''):
                new_task = Task.objects.create(user=user,title=title,category=Category.objects.get(id = category),start_time=start_time,end_time=end_time)
                new_task.save()
                messages.success(request, "your new task is added!")
               
                return redirect('home')
            new_task = Task.objects.create(user=user,title=title,category=Category.objects.get(id = category),start_time=start_time)            
            messages.success(request, "your new task is added!")
           
            return redirect('tasks:home')
        return render(request,'home.html', {'form':form, 'tasks':tasks})


class TaskUpdateView(LoginRequiredMixin,View):
    form_class = DetailForm
    initial = {"key":"value"}
    def get(self, request,pk):
        task = Task.objects.get(pk=pk)
        form = self.form_class(instance=task)
        return render(request, 'detail.html', {'form':form})
        
        
    def post(self, request, pk):
        print(pk)
        task = get_object_or_404(Task, pk=pk)
        form = self.form_class(instance=task,data=self.request.POST)
        print(task.pk)
        if form.is_valid():
            form.save(commit=True)
            u = request.POST
            is_complete = u.get('is_complete')
            if is_complete=='on':
                task.is_complete = True
            else:
                task.is_complete=False
            task.save()
            return redirect('tasks:detail',pk=pk)
        print(task.title)
        context = {'pk':pk}
        return redirect('update', pk=pk)


class TaskDetailView(LoginRequiredMixin,View):   
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        context = {'title':task,
                   'category':task.category,
                   'is_complete':task.is_complete,
                   'description':task.description,
                   'start_time':task.start_time,
                   'end_time':task.end_time,
                   'created_time':task.created_time,
                   'updated_time':task.updated_time,
                   'pk':pk}
        return render(request, 'task_detail.html', context)
    def post(self, request, pk):  
        return redirect('tasks:update',pk=pk)
class DeleteTaskView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:home")
    template_name = "delete.html"
    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user) 