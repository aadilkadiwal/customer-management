from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('products/' ,views.products, name="products"),
    path('customer/', views.customer, name="customer"),
]