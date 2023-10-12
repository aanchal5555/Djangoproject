from django.db import models

# Create your models here.

class userauthentication(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username


