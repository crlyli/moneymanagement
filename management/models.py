from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    """User inputs all types of income"""
    INCOME_TYPE = (
        (1, 'Paycheck'),
        (2, 'Childsupport'),
        (3, 'Foodstamps'),
        (4, 'TANF'),
        (5, 'SocialSecurity'),
        (6, 'CAPS'),
        (7, 'Other')
    )
    INCOME_FREQENCY = (
        (1, 'Weekly'),
        (2, 'Bi-Weekly'),
        (3, 'Monthly'),
        (4, 'Yearly')
    )
    type = models.IntegerField(choices=INCOME_TYPE, default=7)
    frequency = models.IntegerField(choices=INCOME_FREQENCY, default=7)
    image = models.ImageField(upload_to='', null=True)
    amount = models.DecimalField(max_digits=None, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "incometype: {}, income frequency: {}, amount: {}".format(self.frequency,
                                                                         self.type,
                                                                         self.amount)


class MainBill(models.Model):
    """User inputs main bills."""
    TYPE = (
        (1, 'Mortgage'),
        (2, 'Escrow'),
        (3, 'Rent'),
        (4, 'Electric'),
        (5, 'Water'),
        (6, 'Utility Gas'),
        (7, 'Trash'),
        (8, 'Car Payment'),
        (9, 'Car Insurance'),
        (10, 'Credit Card'),
        (11, 'Student Loans'),
        (12, 'Child Support'),
        (13, 'Student Loans'),
        (14, 'Credit Card'),
        (15, 'Phone'),
        (16, 'Other')
    )

    FREQENCY = (
        (1, 'Weekly'),
        (2, 'Bi-Weekly'),
        (3, 'Monthly'),
        (4, '3 months'),
        (5, '6 months'),
        (7, 'Yearly')
    )

    type = models.IntegerField(choices=TYPE)
    frequency = models.IntegerField(choices=FREQENCY)
    image = models.ImageField(upload_to='')
    amount = models.DecimalField(max_digits=None, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "Bill Type: {}, Bill Frequency: {}, Bill Amount: {}".format(self.type,
                                                                           self.frequency,
                                                                           self.amount)


class ExpendableBill(models.Model):
    """User Inputs Expendable Bills"""
    Type=(
        (1, 'Cable'),
        (2, 'Internet'),
        (3, 'Gym Membership'),
        (4, 'Other')
    )

    type = models.IntegerField(choices=TYPE)
    frequency = models.IntegerField(choices=FREQENCY)
    image = models.ImageField(upload_to='')
    amount = models.DecimalField(max_digits=None, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "Bill Type: {}, Bill Frequency: {}, Bill Amount: {}".format(self.type,
                                                                           self.frequency,
                                                                           self.amount)

class Essential(models.Model):
    TYPE = (
        (1, 'Food'),
        (2, 'Dr Visit'),
        (3, 'Prescriptions'),
        (4, 'Car Gasoline'),
        (5, 'Car Repairs'),
        (6, 'Home Repairs'),
        (7, 'Clothing'),
        (8, 'Other')
    )

    FREQENCY = (
        (1, 'Weekly'),
        (2, 'Bi-Weekly'),
        (3, 'Monthly'),
        (4, '3 months'),
        (5, '6 months'),
        (7, 'Yearly')
    )

    type = models.IntegerField(choices=TYPE)
    frequency = models.IntegerField(choices=FREQENCY)
    image = models.ImageField(upload_to='')
    amount = models.DecimalField(max_digits=None, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "Bill Type: {}, Bill Frequency: {}, Bill Amount: {}".format(self.type,
                                                                           self.frequency,
                                                                           self.amount)

#Determine nonessential items or figure out better labeling system
class NonEssential(models.Model):
    """User Inputs Nonessential items"""
    TYPE = (
        (1, 'Other')
    )

    FREQENCY = (
        (1, 'Weekly'),
        (2, 'Bi-Weekly'),
        (3, 'Monthly'),
        (4, '3 months'),
        (5, '6 months'),
        (7, 'Yearly')
    )

    type = models.IntegerField(choices=TYPE)
    title = models.CharField(max_length=20)
    frequency = models.IntegerField(choices=FREQENCY)
    image = models.ImageField(upload_to='')
    amount = models.DecimalField(max_digits=None, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "Bill Type: {}, Bill Frequency: {}, Bill Amount: {}".format(self.type,
                                                                           self.frequency,
                                                                           self.amount)

#Add Item and RecieptItem modesl to testK
class Item(models.Model):
    """List of items from reciept"""
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_length=None, decimal_places=2)

    def __str__(self):
        return "Name: {}  Amount: {}".format(self.name,

                                             self.amount)


class RecieptItem(models.Model):
    """Reciept image and list of items linked to the Item model."""
    image = models.ImageField(upload_to='')
    item = models.ManyToManyField(Item)

    def __str__(self):
        return "Items: {}".format(self.item)
