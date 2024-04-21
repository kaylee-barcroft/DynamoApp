from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('singleorigins/', views.SingleOriginListView.as_view(), name='single-origins'),
    path('singleorigin/<int:pk>/', views.SingleOriginDetailView.as_view(), name='single-origin-detail'),
    path('singleorigin/create', views.createSingleOrigin, name='create-single-origin'),
    path('singleorigin/<int:pk>/update', views.updateSingleOrigin, name='update-single-origin'),
    path('singleorigin/<int:pk>/delete', views.deleteSingleOrigin, name='delete-single-origin'),
    path('subscriptions/', views.SubscriptionsListView.as_view(), 'subscriptions'),
    path('payment/', views.process_payment, name='process_payment'),

    #user accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='register_page'),
    #django.contrib.auth.urls maps the following urls:
    # accounts/ login/ [name='login']
    # accounts/ logout/ [name='logout']
    # accounts/ password_change/ [name='password_change']
    # accounts/ password_change/done/ [name='password_change_done']
    # accounts/ password_reset/ [name='password_reset']
    # accounts/ password_reset/done/ [name='password_reset_done']
    # accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/ reset/done/ [name='password_reset_complete']
]