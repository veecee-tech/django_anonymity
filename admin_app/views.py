from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from account.models import Account
from reports.models import Report

@login_required
def dashboard(request):


    if not request.user.role == 2:
        messages.error(request, 'Access Denied')
        return redirect('account:login')

    users = Account.objects.filter(role=3)
    reports = Report.objects.all().order_by('-created_at')


    

    context = {
        'users': users,
        'reports': reports,
        
    }
    return render(request, 'admin_app/index.html', context)

def acknowledge(request, id):
    report = Report.objects.get(id=id)
    report.status = "acknowledged"

    report.save()

    return redirect('admin_app:dashboard')
