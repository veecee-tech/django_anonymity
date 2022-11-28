from django.contrib import admin
from blog.models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    ordering = ['created_at']


admin.site.register(Blog, BlogAdmin)