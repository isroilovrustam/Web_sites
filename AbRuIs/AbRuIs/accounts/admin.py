from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm
# from .models import UserModel
# # Register your models here.
#
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     models = UserModel
#     list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('age',)}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('age',)}),
#     )
#
#
# admin.site.register(UserModel, CustomUserAdmin)