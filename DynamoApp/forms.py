from django.forms import ModelForm
from .models import SingleOrigin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SingleOriginForm(ModelForm):
    class Meta:
        model = SingleOrigin
        fields = '__all__'