from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import *
from .forms import EmailForm
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model





def index(request):
    return render(request,'landingpage.html')

def admin(request):
    return redirect('/admin/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "Email already taken")
            return redirect('/register/')
        
        user =User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email=username,
            password = password
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully")
        return redirect('/login/')
    return render(request, 'register.html')
        
    

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username,password = password )
        
        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/home/')
    
    return render(request,'login.html')
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.contrib.auth import get_user_model

def logout_page(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/login/")
def home(request):
    evt=Event.objects.all()
    task=Task.objects.all()
    context = {
         'events':evt,
         'tasks': task            
     }
    return render(request,'index.html',context)

@login_required(login_url="/login/")
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        message=request.POST.get('message')
        Volunteer.objects.create(name=name,date=dob,email=email,message=message) 
        
    return render(request,'voluteer.html')

@login_required(login_url="/login/")
def event(request):
    evt=Event.objects.all()
    context = {
         'events':evt,          
     }
    return render(request,'event.html',context)


def admin_check(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(admin_check, login_url='/login/')
def send_email(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            volunteer = form.cleaned_data['volunteer']
            message = form.cleaned_data['message']

            subject = 'Message from the NGO'
            from_email = 'amlananshu6a@gmail.com'
            recipient_list = [volunteer.email]

            send_mail(subject, message, from_email, recipient_list)

            return redirect('home')  # Redirect to a thank-you page or any other desired page

    return render(request, 'email.html', {'form': form})

def joinevent(request,id):
    events=Event.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        JoinEvent.objects.create(event=events,name=name,email=email)
        return redirect('home') 
    return render(request,'joineventform.html',{'events':events})





    



    


