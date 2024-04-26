from django.forms import ModelForm
from .models import SingleOrigin, Subscription, Customer, Manager, Plan
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


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'