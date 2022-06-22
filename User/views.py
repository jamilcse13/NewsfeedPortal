from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from NewsApp import views
from django.contrib.auth.decorators import login_required

from .forms import SettingForm, SignUpForm, PersonCreationForm
from .models import Setting

# Create your views here.
def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
        
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()

            messages.success(request, "Your account has been created successfully!")

            return redirect('signin')
    
    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            fname = user.first_name
            return redirect(home)
            # return render(request, "home.html", {'fname': fname})
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Signed Out Successfully!")
    return redirect('home')


@login_required(login_url='signin')
def settings(request):
    context = {}
    form = SettingForm(request.POST or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            country = request.POST['country']
            source = request.POST['source']
            setting_data = Setting.objects.create(country=country, source=source)
            setting_data.save()

            return redirect('setting')
    return render(request, 'user/settings.html', context)


# same method like settings() but tried in another way
@login_required(login_url='signin')
def setting_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setting_add')
    return render(request, 'user/settings.html', {'form': form})
