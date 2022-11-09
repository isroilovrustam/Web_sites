from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        models = CustomUser
        fields = ('username', 'first_name', 'last_name', 'age')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        models = CustomUser
        fields = ('username', 'first_name', 'last_name', 'age')
