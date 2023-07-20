from django.shortcuts import render, redirect
from  django.views import View
from .forms import RegistrationForm, LoginForm
from .models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required



class RegistrationView(View):
    form_class = RegistrationForm
    initial = {"key":"value"}
    template_name = "registration.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request ,self.template_name , {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
        
            email = request.POST['email']
            password = request.POST['password']
            password1 = request.POST['password1']
            if password == password1:
                new_user = User.objects.create(email=email,password=password)
                messages.success(request, "registration was successfully!")
                login(request, new_user)
                return render(request, 'home.html')
            messages.error(request, 'password doesnt mached')
            return render(request, self.template_name, {})
        return render(request, self.template_name, {'form':form})
    


class LoginView(View):
    form_class = LoginForm
    initial = {"key":"value"}
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request ,self.template_name , {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            email = request.POST['email']
            password = request.POST['password']                
            user = authenticate(request, username=email, password=password)           
            if user is not None:        
                login(request, user)
                return redirect('tasks:home')
            messages.error(request, 'your email or password is not true')
            return render(request, self.template_name, {'form':form})
        return render(request, self.template_name, {'form':form})

    
    # def form_valid(self, form):
    #     self.form_class.instance.password1 = self.request.user.password
    #     return super().form_valid(self.form_class)


# @login_required
# @permission_required   
def logout_view(request):
    if request.method == 'GET':
        return render(request, 'logout.html', {})
    if request.method == 'POST':
        logout(request)
        messages.info(request, "Logged out successfully!")
        return render(request,"login.html",{})














