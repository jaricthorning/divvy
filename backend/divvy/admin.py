from django.contrib import admin
from .models import Expense

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'paidBy')

admin.site.register(Expense, ExpenseAdmin)
