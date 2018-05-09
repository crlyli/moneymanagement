from django.test import TestCase
from management import models


class IncomeTestCase(TestCase):
    fixtures = [inital_data.json]

    def setUp(self):
        pass

    def test_income_string(self):
        """Verify __str__ returns with proper formatting. """
        income = models.Income.objects.get(pk=1)
        self.assertEqual(income.__str__(),)#income,type


class MainBillsTestCase(TestCase):
    fixtures = [inital_data.json]

    def setUp(self):
        pass

    def test_mainbill_string(self):
        """ Verifying __str__ returns with proper formatting. """
        mainbill = models.MainBill.objects.get(pk=1)
        self.assertEqual(mainbill.__str__(), ) #bill,amount


class ExpendableBillsTestCase(TestCase):
    fixtures = [inital_data.json]

    def setUp(self):
        pass

    def test_expendablebill_string(self):
        """ Verify __str__ returns with proper formating."""
        expendablebill= models.ExpendableBill.objects.get(pk=1)
        self.assertEqual(expendablebill.__str__(), )#bill amount


class EssentialTestCase(TestCase):
    fixture = [inital_data.json]

    def setUp(self):
        pass

    def test_essential_string(self):
        """Verify __str__ returns with proper formating."""
        essential = models.Essential.objects.get(pk=1)
        self.assertEqual(essential.__str__(),) #item amount

class NonEssentialTestCase(TestCase):
    fixtures = [inital_data.json]

    def setUp(self):
        pass

    def test_nonessential_string(self):
        """Veryify __str__ returns with proper formating."""
        nonessential = models.NonEssential.objects.get(pk=1)
        self.assertEqual(nonessential.__str__(), )  # item amount

class RecieptbyItemTestCase(TestCase):
    fixtures = [inital_data.json]

    def setUp(self):
        pass

    def test_recieptbyitem_string(self):
        """Veryify __str__ returns with proper formating."""
        recieptbyitem = models.RecieptItem.objects.get(pk=1)
        self.assertEqual(recieptbyitem.__str__(), )  # item amount