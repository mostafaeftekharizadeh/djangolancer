from rest_framework import serializers
from .models import Count,Deposit,Withdraw,Account

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields =  ['party','sheba','card','name','bankname','active'
                    ]
        # ordering_fields = ['title']
        # nested_depth = 2
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields =  ['count',
                    'party',
                    'amount',
                    'date',
                    'transaction',
                    'status'
                    ]
        ordering_fields = ['title']
        nested_depth = 2
class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields =  ['count',
                    'party',
                    'amount',
                    'date',
                    'transaction',
                    'to_account',
                    'acc_name',
                    'status'
                    ]
        ordering_fields = ['acc_name']
        nested_depth = 2
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields =  ['count',
                    'party',
                    'email',
                    'name',
                    'pos',
                    'date',
                    'amount',
                    'de_wi',
                    'balance'
                    ]
        ordering_fields = ['name']
        nested_depth = 2