from django.db import models


class Customer(models.Model):
    email = models.CharField(max_length=255, unique=True)
    
    def __str__(self) -> str:
        return f'{self.email}'