from django.http import HttpRequest
from django.shortcuts import render

from customers.forms import CustomerForm
from robots.models import Robot
from customers.models import Customer
from orders.models import Order


def process_ordering(request: HttpRequest, serial):
    robot = Robot.objects.filter(serial=serial, is_ordered=False)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Customer.objects.filter(email=email).exists():
                customer = Customer.objects.get(email=email)
            else:
                customer = Customer.objects.create(email=email)
            order = Order.objects.create(
                customer=customer,
                robot_serial=serial,
                status = 1 if robot.exists() else 2
            )
            if robot.exists():
                robot_obj = robot.first()
                robot_obj.is_ordered = True
                robot_obj.save()
            request.session['customer_id'] = customer.id
            return render(request, 'customers/success.html', {'order': order})
    else:
        form = CustomerForm()
        return render(
            request, "customers/register.html", {"form": form, "serial": serial}
        )
