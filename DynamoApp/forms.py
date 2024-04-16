from django.forms import ModelForm
from .models import SingleOrigin, Customer, Manager
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SingleOriginForm(ModelForm):
    class Meta:
        model = SingleOrigin
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']