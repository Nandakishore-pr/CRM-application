from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'you have looged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'home.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'you have logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have registered successfully.')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed.')
                return redirect('register_user')
        else:
            # If the form is not valid, render the template again with the invalid form
            messages.error(request, 'Please fix the errors below.')
            return render(request, 'register_user.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register_user.html', {'form': form})