import unittest

from django.db.utils import IntegrityError

from .models import (
    Bank,
    BankBranch,
)


class BankTestCase(unittest.TestCase):
    def setUp(self):
        Bank.objects.create(name="ABC")
        Bank.objects.create(name="SAIB")

    def test_bank_model(self):
        """Animals that can speak are correctly identified"""
        ABC = Bank.objects.get(name="ABC")
        SAIB = Bank.objects.get(name="SAIB")
        self.assertEqual(ABC.__str__(), 'ABC')
        self.assertEqual(SAIB.__str__(), 'SAIB')


class BankBranchTestCase(unittest.TestCase):
    def setUp(self):
        bank = Bank.objects.create(name="TEST")
        BankBranch.objects.create(name=None, address="FakeFake", bank=None)
        BankBranch.objects.create(name="Test", address="address adress", bank=bank)

    def test_create_bankbranch(self):
        bank = Bank.objects.create(name="TEST")
        bb1 = BankBranch.objects.create(name="Test", address="address adress", bank=bank)
        bb2 = BankBranch(name=None, address="FakeFake", bank=None)
        self.assertRaises(IntegrityError, bb2.save)
        self.assertEqual(bb1.__str__(), 'Test')
