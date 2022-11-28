from django.shortcuts import render
from blog.models import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def blog_list(request):

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

    return render(request, 'blog/blog.html', context)
