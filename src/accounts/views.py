from django.shortcuts import redirect, render
from .models import (
    Customer,
    Product,
    Order
)
from .forms import OrderForm

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

def products(request):

    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):

    customer = Customer.objects.get(id=pk)
    orders = customer.orders.all()
    order_count = orders.count()

    context = {
        'customer': customer, 'orders': orders, 'order_count': order_count
    }

    return render(request, 'accounts/customer.html', context)       

def create_order(request):

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form': form}

    return render(request, 'accounts/order.html', context)

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

def delete_order(request, pk):

    order = Order.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect('home-page')

    context = {'order': order}

    return render(request, 'accounts/delete.html', context)    