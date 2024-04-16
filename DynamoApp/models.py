from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.models import User, Group

# Create your models here.


class SingleOrigin(models.Model):
    farm = models.CharField(max_length=200)
    about = models.CharField(max_length=3000)
    roast_profile = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True)
    available = models.BooleanField(default=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.farm

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('single-origin-detail', args=[str(self.id)])
    

class Manager(Group):
    managerUser = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


class Customer(Group):
    customerUser = models.OneToOneField(User, null=True, on_delete=models.CASCADE)