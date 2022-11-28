from django.db import models
from account.models import Account
# Create your models here.


class Report(models.Model):

    STATUS_CHOICE = (
        ('pending', 'PENDING'),
        ('acknowledged', 'ACKNOWLEDGED'),

    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='reporter')
    crime_occuring_now = models.CharField(max_length=10)
    location = models.CharField(max_length=50, null = True)
    regarding = models.CharField(max_length=255, null = True)
    crime_type = models.CharField(max_length=255, null = True)
    details = models.TextField(null = True)
    file = models.FileField(upload_to='files/', null = True)
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, default='pending', max_length=20)


    def __str__(self):
        return f"{self.user}"