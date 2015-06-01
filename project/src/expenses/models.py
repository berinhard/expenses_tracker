#coding:utf-8
from django.db import models


class Expense(models.Model):
    CATEGORIES = (
        (u'f', u'Food'),
        (u'd', u'Drinking'),
        (u't', u'Travel'),
    )

    category = models.CharField(max_length=1, choices=CATEGORIES)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    description = models.TextField(default='')
