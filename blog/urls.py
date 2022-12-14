from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('list/', views.blog_list, name='blog'),
    path('details/<int:id>/', views.blog_details, name='blog_details'),
]
