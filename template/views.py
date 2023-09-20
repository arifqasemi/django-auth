from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.views.generic import FormView
from .models import User
from .forms import LoginForm,RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from django.contrib.auth import authenticate, login

# Create your views here.
@method_decorator(login_required, name='dispatch')

class HomeView(View):
    def get(self, request):
        return render(request, "template/home.html")

  
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def LoginView(request):
    error_message = None  # Initialize error_message to None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=email, password=password)

            if user is not None:
               
                login(request, user)
                
                return redirect('home')
            else:
                
                error_message = "Invalid username or password. Please try again."
        else:
            error_message = "Form validation failed. Please check your input."

    else:
        form = LoginForm()

    return render(request, 'template/login.html', {'form': form, 'error_message': error_message})




class ProfileView(FormView):
    form_class = ProfileForm
    model = User
    template_name = "template/profile.html"
    # success_url = "home"
    def form_valid(self, form):
        instance = form.save()
        return super().form_valid(form)

    
class RegisterView(FormView):
    form_class = RegisterForm
    model = User
    template_name = "template/register.html"
    success_url = "login"
    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, 'Your account has been created. Please log in.') 
        return super().form_valid(form)