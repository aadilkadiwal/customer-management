from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('order/new/', views.create_order, name="create-order"),
    path('order/<int:pk>/', views.update_order, name="update-order"),
    path('order/delete/<int:pk>/', views.delete_order, name="delete-order"),
]