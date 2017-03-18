from rest_framework import serializers
from bank.models import BankAccount


class AccountDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('credit', )
