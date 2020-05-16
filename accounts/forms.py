from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'last_name', 'first_name', 'email']

class CUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email']
