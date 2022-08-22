from django.contrib import admin
from .models import Count,Deposit,Withdraw,Account



class CountAdmin(admin.ModelAdmin):
    pass
class DepositAdmin(admin.ModelAdmin):
    pass
class WithdrawAdmin(admin.ModelAdmin):
    pass
class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Count, CountAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(Account, AccountAdmin)
