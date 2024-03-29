from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('singleorigin/<int:pk>/', views.SingleOriginDetailView.as_view(), name='single-origin-detail'),
]