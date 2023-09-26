from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from customers.forms import CustomerForm
from orders.models import Order
from robots.models import Robot


def get_email_from_customer(request: HttpRequest, model, version):
    robot = get_object_or_404(Robot, model=model, version=version)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            robot.is_ordered = True
            robot.save()
            order = Order.objects.create(
                customer=customer,
                robot_serial=robot.serial,
                status = 1 if robot.is_exists else 2)
            return render(request, "customers/success.html", {
                'robot': robot, 'order': order
            })
        else:
            return redirect(request.META["HTTP_REFERER"])
    else:
        
        form = CustomerForm()
        return render(
            request,
            "customers/register.html",
            {"form": form, "robot": robot}
        )


