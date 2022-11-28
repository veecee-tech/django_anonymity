from django.urls import path 
from . import views

app_name = 'reports'


urlpatterns = [
    path('', views.report, name='make_report')
]
