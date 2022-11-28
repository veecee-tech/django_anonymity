from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    if not request.user.role == 3:
        messages.error(request, 'Access Denied')
        return redirect('account:login')
    return render(request, 'reporter/dashboard.html')