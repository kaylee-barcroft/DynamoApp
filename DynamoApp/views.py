from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # render the HTML template with data from the context variable.
    return render(request, 'DynamoApp/index.html')
