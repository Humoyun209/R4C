from django.db import models

from customers.models import Customer


class Order(models.Model):
    ORDERED = 1
    PENDING = 2
    STATUSES = [
        (ORDERED, 'Заказан'),
        (PENDING, 'В ожидании')
    ]
    customer = models.ForeignKey(Customer, 
                                 on_delete=models.CASCADE, 
                                 related_name='orders')
    robot_serial = models.CharField(max_length=5)
    status = models.SmallIntegerField(choices=STATUSES)
    
    def __str__(self) -> str:
        return f'Order#{self.id} - {self.robot_serial}'