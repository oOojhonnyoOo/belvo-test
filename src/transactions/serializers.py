from rest_framework import serializers
from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'reference', 
            'email', 
            'date', 
            'amount', 
            'type', 
            'category'
        ]

    def validate(self, attrs):
        amount = attrs.get('amount')
        transaction_type = attrs.get('type')

        if transaction_type == 'outflow' and amount > 0:
            raise serializers.ValidationError("Outflow transactions must have a negative amount.")
        elif transaction_type == 'inflow' and amount < 0:
            raise serializers.ValidationError("Inflow transactions must have a positive amount.")

        return attrs

"""
    def clean(self):
        if self.amount < 0 and self.type != 'outflow':
            raise ValidationError("Invalid transaction type for negative amount")
        if self.amount >= 0 and self.type != 'inflow':
            raise ValidationError("Invalid transaction type for positive or zero amount")
"""