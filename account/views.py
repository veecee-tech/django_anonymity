from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from .models import Account, UserProfile
# Create your views here.


def register(request):

    if request.method == 'POST':
        forms = UserCreationForm(request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request, "Registration Successful")
            return redirect("account:login")
    else:
        forms = UserCreationForm()
        
    context = {
        'forms': forms,
       
    }

    return render(request, 'account/register.html', context)

def login_user(request):
   

    if request.method == "POST":
        
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        
        if user:

            login(request, user)
            if user.role == 1:
                logout(request)
                messages.error(request, 'Access Denied')
                return redirect("account:login")
            if user.role == 2:                
                return redirect("admin_app:dashboard")   
            if user.role == 3:
                return redirect('reporter:dashboard')                            
        else:
            messages.error(request, "Invalid email or Password")
            return redirect("account:login")

    return render(request, 'account/login.html')



def logout_user(request):
    logout(request)
    return redirect('home:home')

@login_required
def change_password(request):
    user = Account.objects.get(username__exact = request.user.username)
    if request.method == 'POST':

        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        success_check = user.check_password(old_password)

        if success_check:

            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password Changed Succssfully")
                return redirect('change_password')
            else:
                messages.error(request, 'Password does not match')
                return redirect('change_password')
        else:
            messages.error(request, 'Old password incorrect')

        
    return render(request, 'authentication/change_password.html')

        