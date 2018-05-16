from django.db import models
from management import choices


class Income(models.Model):
    """User inputs all types of income"""

    type = models.IntegerField(choices=choices.INCOME_TYPE, default=7)
    frequency = models.IntegerField(choices=choices.FREQENCY, default=7)
#    image = models.ImageField(upload_to='management\static\income', null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "incometype: {}, income frequency: {}, amount: {}".format(self.frequency,
                                                                         self.type,
                                                                         self.amount)


class MainBill(models.Model):
    """User inputs main bills."""

    type = models.IntegerField(choices=choices.MAINBILL_TYPE)
    frequency = models.IntegerField(choices=choices.FREQENCY)
#    image = models.ImageField(upload_to='')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "Bill Type: {}, Bill Frequency: {}, Bill Amount: {}".format(self.type,
                                                                           self.frequency,
                                                                           self.amount)


class ExpendableBill(models.Model):
    """User Inputs Expendable Bills"""

    type = models.IntegerField(choices=choices.EXPENDABLEBILL_TYPE)
    frequency = models.IntegerField(choices=choices.FREQENCY)
#    image = models.ImageField(upload_to='')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "Bill Type: {}, Bill Frequency: {}, Bill Amount: {}".format(self.type,
                                                                           self.frequency,
                                                                           self.amount)


class Essential(models.Model):

    type = models.IntegerField(choices=choices.ESSENTIALBILL_TYPE)
    frequency = models.IntegerField(choices=choices.FREQENCY)
#    image = models.ImageField(upload_to='')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "Bill Type: {}, Bill Frequency: {}, Bill Amount: {}".format(self.type,
                                                                           self.frequency,
                                                                           self.amount)


#Determine nonessential items or figure out better labeling system
class NonEssential(models.Model):
    """User Inputs Nonessential items"""

    type = models.IntegerField(choices=choices.NONESSENTIAL_TYPE)
    title = models.CharField(max_length=20)
    frequency = models.IntegerField(choices=choices.FREQENCY)
#    image = models.ImageField(upload_to='')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=150)

    def __str__(self):
        return "Bill Type: {}, Bill Frequency: {}, Bill Amount: {}".format(self.type,
                                                                           self.frequency,
                                                                           self.amount)


#Add Item and RecieptItem modesl to testK
class Item(models.Model):
    """List of items from reciept"""
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Name: {}  Amount: {}".format(self.name,
                                             self.amount)


class RecieptItem(models.Model):
    """Reciept image and list of items linked to the Item model."""
#    image = models.ImageField(upload_to='')
    item = models.ManyToManyField(Item)

    def __str__(self):
        return "Items: {}".format(self.item)
