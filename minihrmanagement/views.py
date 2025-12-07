from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('leave_request')
        else:
            error = "Invalid username or password."
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

  

def signup_view(request):
    message = None  # For success message
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists!"})

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)

        login(request, user)

        # Success message
        message = "Registration successful! Welcome, " + username

        return render(request, "signup.html", {"message": message})

    return render(request, "signup.html")


def home(request):
    return redirect('login')
    

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def forget_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        try:
            user = User.objects.get(email=email)
            request.session['user_email'] = email  # Temporary save
            return redirect('reset_password')  # Go to reset page
        except User.DoesNotExist:
            messages.error(request, "This email does not exist!")
    
    return render(request, "forget_password.html")
    




def reset_password(request):
    email = request.session.get('user_email')

    if not email:
        return redirect('forget_password')

    if request.method == "POST":
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
        else:
            user = User.objects.get(email=email)
            user.password = make_password(password1)
            user.save()

            request.session.pop('user_email')  # Clear temporary email
            messages.success(request, "Password Successfully Updated!")
            return redirect('login')

    return render(request, "reset_password.html")












