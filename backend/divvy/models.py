from django.db import models

# Create your models here.

class Expense(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField()
    paidBy = models.CharField(max_length=20)

    def __str__(self):
        return self.name

