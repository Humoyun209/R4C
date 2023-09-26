from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from orders.models import Order

from robots.models import Robot


@receiver(pre_save, sender=Robot)
def order_status_changed(sender, instance, **kwargs):
        old_robot = Robot.objects.get(id=instance.id)
        if not old_robot.is_exists and instance.is_exists:
            orders = Order.objects.filter(status=2, robot_serial=instance.serial)
            for order in orders:
                order.status = 1
                order.save()
                subject = "Робот тепер сушествует!!!"
                message = f"""Добрый день! \nНедавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}. \nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"""
                from_email = "test@mail.ru"
                to_emails = [order.customer.email]
                send_mail(subject, message, from_email, to_emails)
