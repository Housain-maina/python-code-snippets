from django.db import models
from django.utils import timezone

class Phone(models.Model):
    name = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=150)
    year = models.CharField(default=timezone.now().year, max_length=4)
    operating_system = models.CharField(max_length=50)


    def __str__(self) -> str:
        return f"{self.manufacturer} {self.name} {self.year}"
