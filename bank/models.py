from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Client(AbstractBaseUser):
    username = models.CharField(_('name'), max_length=64, default=None, blank=False)
    first_name = models.CharField(_('first name'), max_length=15, default=None, blank=False)
    last_name = models.CharField(_('last name'), max_length=15, default=None, blank=False)

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def get_username(self):
        return self.username

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name()


class Bank(models.Model):
    name = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name


class BankBranch(models.Model):
    name = models.CharField(_('name'), max_length=382, blank=False)
    address = models.TextField(_('address'), max_length=1023, blank=False)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank_branches', verbose_name=(_('bank')))

    class Meta:
        verbose_name_plural = _('Bank Branches')

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='bank_account')
    branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE, verbose_name=(_('The bank branch')))
    credit = models.PositiveIntegerField(_('Credit'), default=0, blank=False)

    class Meta:
        verbose_name_plural = _('Bank Accounts')

    def __str__(self):
        return "%s_%d" % (self.user.__str__(), self.id)


class Employee(AbstractUser):
    is_manager = models.BooleanField(_('Is he a manager'), default=0)
    is_organization = models.BooleanField(_('Is this account is an organization'), default=0)
    branch = models.ForeignKey(BankBranch, blank=True, null=True, verbose_name=_('Bank Branch'))
    bank = models.OneToOneField(Bank, null=True, blank=True, default=None, related_name='manager', verbose_name=_('Bank'))

    class Meta:
        verbose_name_plural = _('Employees')

    @property
    def hierarchy(self):
        return Employee.objects.filter(branch=self.branch)

    def __str__(self):
        if self.is_manager:
            return "Manager of %s at %s" % (self.branch.name, self.bank.name)
        elif self.is_organization:
            return self.bank.name
        else:
            try:
                return "%s at %s" % (self.username, self.branch.name)
            except AttributeError:
                return self.username
