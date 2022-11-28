from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django_currentuser.middleware import get_current_authenticated_user

from .models import Account, UserProfile


# class UserLoginForm(forms.Form):
#     email = forms.CharField(widget=forms.Emai(attrs={"class": "form-control", "placeholder": "email"}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={"class": "p-3 w-full outline-[#1676F3] outline-1 rounded-md border border-[gainsboro]", "placeholder": "Confirm Password", "id":"confirm_password"}))

    class Meta:
        model = Account
        fields = ['email', 'full_name']

    def clean_email(self):

        email = self.cleaned_data.get('email')
        qs = Account.objects.filter(email=email)

        if qs.exists():
            raise forms.ValidationError("email already exists") 
        return email

    def clean(self):

        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")

        if password is not None and password != password_2:
            self.add_error("password_2", "Your password must match")
        return cleaned_data

    def save(self,commit=True):
        user = super().save(commit=False)
        user.role = 3
        user.is_active = True
        user.is_staff = True
       
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args,**kwargs)
        
        self.fields['email'].widget.attrs['class'] = "p-3 outline-[#1676F3] outline-1 rounded-md border border-[gainsboro]"
        self.fields['email'].widget.attrs['placeholder'] = "Johndoe@gmail.com"
        self.fields['email'].widget.attrs['id'] = "email"

        self.fields['full_name'].widget.attrs['class'] = "p-3 outline-[#1676F3] outline-1 rounded-md border border-[gainsboro]"
        self.fields['full_name'].widget.attrs['placeholder'] = "John Doe"
        self.fields['full_name'].widget.attrs['id'] = "name"
       
        self.fields['password'].widget.attrs['class'] = "p-3 w-full outline-[#1676F3] outline-1 rounded-md border border-[gainsboro]"
        self.fields['password'].widget.attrs['placeholder'] = "Enter password here"
        self.fields['password'].widget.attrs['id'] = "password"


        



class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['email','full_name','role', 'is_staff', 'is_admin', 'is_active']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ['email','full_name', 'password', 'is_staff', 'is_active', 'role', 'is_admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
    def save(self, commit=True):
        
        user = super().save(commit=False)
        
        if commit:
            user.save()
        return user