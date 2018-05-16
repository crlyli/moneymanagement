from django.contrib import admin
from . import models
# Register your models here.


# admin.site.register(MODEL)
admin.site.register(models.Income)
admin.site.register(models.MainBill)
admin.site.register(models.ExpendableBill)
admin.site.register(models.Essential)
admin.site.register(models.NonEssential)
admin.site.register(models.Item)
admin.site.register(models.RecieptItem)
