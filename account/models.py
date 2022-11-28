from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from .views import get_first_names


class MyAccountManager(BaseUserManager):

    def create_user(self, email,full_name, password=None):

        if not email:
            raise ValueError('User must have an email')

        user = self.model(
            email = email,
            full_name = full_name
        )

        user.is_staff = True 
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):

        user = self.create_user(
            email = email,
            full_name=full_name,

        )
        user.is_admin = True
        user.is_staff = True
        user.role = 1
        user.is_active = True
        user.is_superadmin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
        

class Account(AbstractBaseUser):

    USER_TYPE_CHOICES = (
      (1, 'superadmin'),
      (2, 'admin'),
      (3, 'reporter')
      
  )
    email = models.EmailField(max_length=254, unique = True)
    full_name = models.CharField(max_length=50, null=False)
    role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=3)
    #required
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    objects = MyAccountManager()

    def __str__(self):
        return f"{self.email}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    
    
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )

    marital_choice = (
        ("single", "Single"),
        ("married", "Married"),
        ("divorced", "Divorced"),
        ("widowed", "Widowed")
    )
    user = models.OneToOneField(to=Account, related_name="userprofile", null=True, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length = 30, null=True)
    marital_status = models.CharField(choices=marital_choice, max_length=10, null=True)
    location = models.CharField(max_length = 30, null=True)
    occupation = models.CharField(max_length = 30, null=True)
    address = models.CharField(max_length = 100)
    gender = models.CharField(choices=gender_choice, max_length=10, null=True)

    def __str__(self):
        return self.user
    



@receiver(post_save, sender=Account)
def create_profile(sender, instance, created,**kwargs):
   
    if created and instance.role == 3:
        UserProfile.objects.create(user=instance)
    else:
        pass
