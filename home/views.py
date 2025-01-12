from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home/home.html")

def loginUser(request):
    if request.method == 'POST':
        # Retrieve username and password from the POST data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            # If authentication failed, display an error message
            messages.error(request, 'Invalid username or password')

    return render(request, 'home/login.