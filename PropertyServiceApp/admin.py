from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Users, Roles, PropertyTracing, MaintainanceAndLease, LegalIssues, PropertyMonitoring, InvestmentAdvice, OtherServices
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'is_staff')

    list_editable = ('is_staff',)
    # list_filter = ('is_admin',)
    fieldsets = (
        ('Account', {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('fullname', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    add_fieldsets = (
        ('Account', {'fields': ('email', 'username', 'password1', 'password2',)}),
        ('Personal info', {'fields': ('fullname', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',)}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


admin.site.register(Users)

admin.site.register(Roles)

admin.site.register(PropertyTracing)

admin.site.register(MaintainanceAndLease)

admin.site.register(LegalIssues)

admin.site.register(PropertyMonitoring)

admin.site.register(InvestmentAdvice)

admin.site.register(OtherServices)


# admin.site.unregister(Group)
