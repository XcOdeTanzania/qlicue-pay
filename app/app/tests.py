from django.tests import TestCase

from app.deposit import deposit


class DepositTests(TestCase):
    def test_deposit_money(self):
        """Test that amount is deposited"""
        self.assertEqual(deposit(100), 200)
