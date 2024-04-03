from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import SingleOriginForm
from django.contrib import messages

# Create your views here.
def index(request):
    # render the HTML template with data from the context variable.
    current_so_offerings = SingleOrigin.objects.all().filter(available=True)
    return render(request, 'DynamoApp/index.html', {'current_so_offerings':current_so_offerings})

class SingleOriginDetailView(generic.DetailView):
    model = SingleOrigin

class SingleOriginListView(generic.ListView):
    model = SingleOrigin

def createSingleOrigin(request):
    form = SingleOriginForm

    if request.method == 'POST':
        single_origin_data = request.POST.copy()
        form = SingleOriginForm(single_origin_data)
        if form.is_valid():
            form.save()
            
            return redirect('single-origins') # need to reference the pk of the instance
    
    context = {'form': form}
    return render(request, 'DynamoApp/single_origin_form.html', context)


def updateSingleOrigin(request, pk):
    so = SingleOrigin.objects.get(id=pk)
    form = SingleOriginForm(instance=so)

    if request.method == 'POST':
        form = SingleOriginForm(request.POST, instance=so)
        if form.is_valid():
            single_origin = form.save()
            return redirect('single-origin-detail', pk)
    
    context = {'form': form}
    return render(request, 'DynamoApp/single_origin_form.html', context)


def deleteSingleOrigin(request, pk):
    so = SingleOrigin.objects.get(id=pk)

    if request.method == 'POST':
        so.delete()
        messages.success(request, "The single-origin instance has been deleted.")
        return redirect('single-origins')

    context = {'item': so}
    return render(request, 'DynamoApp/single_origin_delete.html', context)