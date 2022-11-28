from django.shortcuts import render
from blog.models import Blog
from django.core.paginator import Paginator
# Create your views here.

def home(request):

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

    return render(request, 'home/index.html', context)

def faq(request):
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

    return render(request, 'home/faq.html', context)
