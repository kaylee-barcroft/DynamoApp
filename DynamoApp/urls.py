from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('singleorigins/', views.SingleOriginListView.as_view(), name='single-origins'),
    path('singleorigin/<int:pk>/', views.SingleOriginDetailView.as_view(), name='single-origin-detail'),
    path('singleorigin/create', views.createSingleOrigin, name='create-single-origin'),
    path('singleorigin/<int:pk>/update', views.updateSingleOrigin, name='update-single-origin'),
    path('singleorigin/<int:pk>/delete', views.deleteSingleOrigin, name='delete-single-origin'),
]