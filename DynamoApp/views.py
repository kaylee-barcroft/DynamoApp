from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from django_project import settings
from .forms import SingleOriginForm, CreateUserForm, SubscriptionForm
from .models import *
from .decorators import unauthenticated_user, allowed_users

import stripe
import datetime


def index(request):
    # render the HTML template with data from the context variable.
    current_so_offerings = SingleOrigin.objects.all().filter(available=True)
    return render(request, 'DynamoApp/index.html', {'current_so_offerings':current_so_offerings})


class SingleOriginDetailView(generic.DetailView):
    model = SingleOrigin


class SingleOriginListView(generic.ListView):
    model = SingleOrigin


@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
def deleteSingleOrigin(request, pk):
    so = SingleOrigin.objects.get(id=pk)

    if request.method == 'POST':
        so.delete()
        messages.success(request, "The single-origin instance has been deleted.")
        return redirect('single-origins')

    context = {'item': so}
    return render(request, 'DynamoApp/single_origin_delete.html', context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            customer = Customer.objects.create(user=user,)
            # portfolio = Portfolio.objects.create()
            # student.portfolio = portfolio
            customer.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)


@login_required(login_url='login')
def subscribe(request):
    form = SubscriptionForm
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        form = SubscriptionForm(request.POST)

        if form.is_valid():
                plan = form.cleaned_data['plan']
                subscription = Subscription(user=request.user,
                                            plan=plan)
                subscription.end_date = subscription.end_date
                subscription.save()
                return redirect('subscriptions')
                
    return render(request, 'DynamoApp/subscribe.html', {'form':form})


        # try:
        #     customer = stripe.Customer.create(
        #         email=request.user.email,
        #         source=request.POST['stripeToken']
        #     )

        #     subscription = stripe.Subscription.create(
        #         customer=customer.id,
        #         items=[
        #             {
        #                 'plan': plan_id
        #             }
        #         ]
        #     )

        #     Subscription.objects.create(
        #         user=request.user,
        #         stripe_customer_id=customer.id,
        #         stripe_subscription_id=subscription.id,
        #         plan_id=plan_id
        #     )

        #     return render(request, 'success.html')
        
        # except stripe.error.CardError as e:
        #     # handle card error
        #     return render(request, 'error.html', {'error': e})
        
        # except Exception as e:
        #     # other errors
        #     return render(request, 'error.html', {'error': e})
    
    #plan_id = 'your_stripe_plan_id'



#@login_required(login_url='login')
class SubscriptionsListView(generic.ListView):
    model = Subscription


def process_payment(request):
    if request.method == 'POST':
        card_number = request.POST['card_number']
        expiry_date = request.POST['expiry_date']
        cvc = request.POST['cvc']
        
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        try:
            charge = stripe.Charge.create(
                amount=1000,  # amount in cents
                currency='usd',
                source={
                    'number': card_number,
                    'exp_month': expiry_date.split('/')[0],
                    'exp_year': expiry_date.split('/')[1],
                    'cvc': cvc
                },
                description='Payment for Django Web App'
            )
            
            # Process successful payment
            return render(request, 'success.html')
        
        except stripe.error.CardError as e:
            # Handle card error
            return render(request, 'error.html', {'error': e})
        
        except Exception as e:
            # Handle other exceptions
            return render(request, 'error.html', {'error': e})