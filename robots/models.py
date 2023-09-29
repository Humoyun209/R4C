from django.db import models
from django.forms import ValidationError
from django.utils import timezone


class Robot(models.Model):
    serial = models.CharField(max_length=5)
    model = models.CharField(max_length=2)
    version = models.CharField(max_length=2)
    created = models.DateTimeField()
    is_ordered = models.BooleanField(default=False)
    
    def clean_serial(self):
        if self.serial != f'{self.model}-{self.version}':
            raise ValidationError('The series fields do not meet the requirements')
    
    def __str__(self) -> str:
        return f'Robot#{self.id} - {self.serial}'
    