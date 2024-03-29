from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic

# Create your views here.
def index(request):
    # render the HTML template with data from the context variable.
    current_so_offerings = SingleOrigin.objects.select_related('singleorigin').all().filter(singleorigin__is_available=True)
    return render(request, 'DynamoApp/index.html')

class SingleOriginDetailView(generic.DetailView):
    model = SingleOrigin