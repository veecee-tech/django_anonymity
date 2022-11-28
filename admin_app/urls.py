from django.urls import path
from . import views

app_name = 'admin_app'

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('ack/<int:id>/', views.acknowledge, name='ack'),
]
