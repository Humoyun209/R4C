from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from customers.models import Customer
from orders.forms import EmailForm
from orders.models import Order


def get_my_orders(request: HttpRequest):
    customer_id = request.session.get("customer_id")
    if customer_id:
        customer_id = int(customer_id)
        customer = get_object_or_404(Customer, id=customer_id)
        orders = Order.objects.filter(customer=customer)
        return render(request, "orders/orders.html", {"orders": orders})
    else:
        return redirect('orders:get_email')


def get_customer_by_email(request: HttpRequest):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            customer = Customer.objects.filter(email=email)
            if customer.exists():
                request.session["customer_id"] = customer.first().id
            return redirect('orders:my_orders')
    else:
        form = EmailForm()
        return render(request, "orders/register.html", {"form": form})
