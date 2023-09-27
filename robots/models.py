from django.db import models
from django.utils import timezone


class Robot(models.Model):
    serial = models.CharField(max_length=5)
    model = models.CharField(max_length=2)
    version = models.CharField(max_length=2)
    created = models.DateTimeField(default=timezone.now)
    is_ordered = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Робот'
        verbose_name_plural = 'Роботы'
        ordering = ['serial']
