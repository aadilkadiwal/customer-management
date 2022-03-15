from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home-page"),
    path('login/' ,views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('user/', views.userPage, name='user-page'),
    path('profile-settings/', views.profileSettings, name='profile-settings'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('order/new/<int:pk>', views.create_order, name="create-order"),
    path('order/<int:pk>/', views.update_order, name="update-order"),
    path('order/delete/<int:pk>/', views.delete_order, name="delete-order"),
]