#coding:utf-8
from django.test import TestCase

from src.expenses.models import Expense


class TestExpenseModel(TestCase):

    def test_category_choices(self):
        expected = (
            (u'f', u'Food'),
            (u'd', u'Drinking'),
            (u't', u'Travel'),
        )
        field = Expense._meta.get_field_by_name('category')[0]
        self.assertEqual(expected, field.choices)
        self.assertEqual(expected, Expense.CATEGORIES)
