# coding:utf-8
from datetime import date

from django.test import TestCase

from src.expenses.models import Expense
from src.expenses.serializers import ExpenseSerializer


class TestExpenseSerializer(TestCase):

    def test_formats_data_correctly(self):
        category = Expense.CATEGORIES[0]
        expense = Expense.objects.create(
            id=42,
            value=10,
            category=Expense.CATEGORIES[0][0],
            date=date(2015, 1, 1),
            description='foo'
        )

        serializer = ExpenseSerializer(expense)

        self.assertEqual(42, serializer.data['id'])
        self.assertEqual(u'10.00', serializer.data['value'])
        self.assertEqual(category[0], serializer.data['category'])
        self.assertEqual(category[1], serializer.data['category_display'])
        self.assertEqual('01/01/2015', serializer.data['date'])
        self.assertEqual('foo', serializer.data['description'])
