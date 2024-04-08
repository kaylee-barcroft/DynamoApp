from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('singleorigins/', views.SingleOriginListView.as_view(), name='single-origins'),
    path('singleorigin/<int:pk>/', views.SingleOriginDetailView.as_view(), name='single-origin-detail'),
    path('singleorigin/create', views.createSingleOrigin, name='create-single-origin'),
    path('singleorigin/<int:pk>/update', views.updateSingleOrigin, name='update-single-origin'),
    path('singleorigin/<int:pk>/delete', views.deleteSingleOrigin, name='delete-single-origin'),
    
    #user accounts
    path('accounts/', include('django.contrib.auth.urls')),
    #django.contrib.auth.urls maps the following urls:
    ## for all: accounts/ 
    ##
    #login/
    #logout/
    #password_change/
    #password_change/done/
    #password_reset/
    #password_reset/done/
    #reset/<uidb64>/<token>/
    #reset/done/
]