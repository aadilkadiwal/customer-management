from accounts.decorators import unauthenticated_user
from django.shortcuts import redirect, render
from .models import (
    Customer,
    Product,
    Order
)
from .forms import OrderForm, CreateUserForm
from django.forms import inlineformset_factory
from .filters import (
    OrderFilter
)
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

def registerPage(request):

    if request.user.is_authenticated:
        return redirect('home-page')
    else:    
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                messages.success(request, 'Account was created for ' + username)
                return redirect('login')

        context = {'form': form}

        return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'accounts/login.html',)  


    context = {}

    return render(request, 'accounts/login.html', context)  

def logoutPage(request):

    logout(request)

    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):

    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    orders_delivered = orders.filter(status="DELIVERED").count()
    orders_pending = orders.filter(status="PENDING").count()
    orders_outfordelivery = orders.filter(status="OUT FOR DELIVERY").count()

    context = {
        'customers': customers, 'orders': orders, 'total_customers': total_customers,
        'total_orders': total_orders, 'orders_delivered': orders_delivered, 'orders_pending': orders_pending,
        'orders_outfordelivery': orders_outfordelivery
        }

    return render(request, 'accounts/dashboard.html', context)

def userPage(request):

    context = {}

    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):

    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):

    customer = Customer.objects.get(id=pk)
    orders = customer.orders.all()
    order_count = orders.count()

    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs

    context = {
        'customer': customer, 'orders': orders, 'order_count': order_count, 'myfilter': myfilter
    }

    return render(request, 'accounts/customer.html', context)       

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request, pk):

    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home-page')

    context = {'formset': formset}

    return render(request, 'accounts/order.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk):
    
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form': form}

    return render(request, 'accounts/order.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request, pk):

    order = Order.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect('home-page')

    context = {'order': order}

    return render(request, 'accounts/delete.html', context)    