from django.db import models
from django.utils import timezone


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=True, null=True)
    model = models.CharField(max_length=2)
    version = models.CharField(max_length=2, unique=True)
    created = models.DateTimeField(default=timezone.now)
    is_exists = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Робот'
        verbose_name_plural = 'Роботы'
        ordering = ['serial']
    
    
        