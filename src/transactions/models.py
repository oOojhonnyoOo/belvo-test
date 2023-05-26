from django.db import models
from enum import Enum
from django.db import connection


class TransactionType(Enum):
    INFLOW = 'inflow'
    OUTFLOW = 'outflow'


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        (TransactionType.INFLOW.value, 'Inflow'),
        (TransactionType.OUTFLOW.value, 'Outflow'),
    ]

    reference = models.AutoField(primary_key=True)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=50)

    class Meta:
        ordering = ['reference']
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'date', 'amount', 'type', 'category'],
                name='unique_transaction'
            )
        ]

