from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import UserProfile
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'is_admin', 'role']
    list_filter = ['is_admin','is_admin', 'role']
    fieldsets = (
        (None, {'fields': ('email','full_name', 'password')}),
        # ('Personal info', {'fields': ('level',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'role')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','full_name', 'password', 'password_2','is_staff','role', 'is_admin','is_active')}
        ),
    )
    search_fields = ['email', 'role']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)