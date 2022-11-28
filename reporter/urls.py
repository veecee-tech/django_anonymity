from django.urls import path
from . import views

app_name = "reporter"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"), 
]
