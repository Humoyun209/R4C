from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from orders.models import Order

from robots.models import Robot


def update_order_status(instance):
    order = Order.objects.filter(robot_serial=instance.serial, status=2)
    if order.exists():
        order = order.first()
        order.status = 1
        order.save()
        subject = "Робот тепер сушествует!!!"
        message = f"""Добрый день! \nНедавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}. \nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"""
        from_email = "test@mail.ru"
        to_emails = [order.customer.email]
        send_mail(subject, message, from_email, to_emails)


@receiver(post_save, sender=Robot)
def order_status_changed(sender, instance, **kwargs):
    if not instance.is_ordered and instance.serial in Order.objects.filter(
        status=2
    ).values_list("robot_serial", flat=True):
        instance.is_ordered = True
        instance.save()
        update_order_status(instance)
