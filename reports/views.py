from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from blog.models import Blog
from reports.models import Report
from django.contrib import messages

from django.contrib.auth.decorators import login_required


@login_required
def report(request):

    if request.user.role == 1:
        messages.error(request, 'Access Denied')
        return redirect('account:login')
    
    if request.user.role == 2:
        messages.error(request, 'Access Denied')
        return redirect('account:login')

    if request.method == 'POST':
        crime_occuring_now = request.POST.get('occuring_now')
        location = request.POST.get('state')
        regarding = request.POST.getlist('regarding')
        crime_type = request.POST.getlist('crime_type')
        details = request.POST.get('detail')
        file = request.FILES['file']

        report = Report()
        report.user = request.user
        report.crime_occuring_now = crime_occuring_now
        report.location = location
        report.regarding = ", ".join(regarding)
        report.details = details
        report.crime_type = ", ".join(crime_type)
        report.file = file

        report.save()

        return redirect('reporter:dashboard')
    blogs = Blog.objects.all().order_by('-created_at')
    latest_5 = Blog.objects.all().order_by('-created_at')[:7]

    paginator = Paginator(blogs, 3)
    page = request.GET.get('pages')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs': blogs,
        'latest_5': latest_5,
        'paged_blogs': paged_blogs

    }

    return render(request, 'reports/report.html', context)