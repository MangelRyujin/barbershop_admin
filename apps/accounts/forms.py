from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(AdminUserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email","is_worker","image","password1","password2")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email","is_worker","image","first_name","last_name")