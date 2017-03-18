from django.contrib import admin
from .models import (
    Bank,
    BankBranch,
    BankAccount,
    Employee,
    Client,
)
from .forms import ClientForm, EmployeeForm


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BankAdmin, self).get_queryset(request=request)
        if request.user.is_superuser:
            return qs
        return qs.filter(manager=request.user)


class BankBranchAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BankBranchAdmin, self).get_queryset(request=request)
        if request.user.is_manager:
            main_bank = Bank.objects.get(employee=request.user)
            return qs.filter(bank=main_bank)
        elif request.user.is_superuser:
            return qs
        else:
            return qs.filter(employee=request.user)


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm

    def get_queryset(self, request):
        qs = super(EmployeeAdmin, self).get_queryset(request=request)
        if request.user.is_manager:
            main_bank = Bank.objects.get(employee=request.user)
            return qs.filter(bank=main_bank)
        else:
            return qs.none()


class ClientAdmin(admin.ModelAdmin):
    form = ClientForm

    def get_queryset(self, request):
        qs = super(ClientAdmin, self).get_queryset(request=request)
        if request.user.is_manager:
            main_bank = Bank.objects.get(employee=request.user)
            return qs.filter(bank_account__branch__bank=main_bank)
        else:
            return qs.none()


class BankAccountAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BankAccountAdmin, self).get_queryset(request=request)
        return qs.filter(branch__employee__in=request.user.hierarchy)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(BankBranch, BankBranchAdmin)
admin.site.register(Client, ClientAdmin)
