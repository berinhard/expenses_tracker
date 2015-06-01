# coding:utf-8
from decimal import Decimal
from datetime import date

from django.core.urlresolvers import reverse
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
        resource_url = reverse('expenses:expense_detail', args=[42])

        self.assertEqual(42, serializer.data['id'])
        self.assertEqual(u'10.00', serializer.data['value'])
        self.assertEqual(category[0], serializer.data['category'])
        self.assertEqual(category[1], serializer.data['category_display'])
        self.assertEqual('2015-01-01', serializer.data['date'])
        self.assertEqual('foo', serializer.data['description'])
        self.assertEqual(resource_url, serializer.data['resource_url'])

    def test_creates_expense(self):
        data = {
            'value': '10.92',
            'category': Expense.CATEGORIES[0][0],
            'description': 'foo',
            'date': '2015-12-31',
        }

        serializer = ExpenseSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        expense = serializer.save()

        self.assertTrue(expense.id)
        self.assertEqual(Decimal('10.92'), expense.value)
        self.assertEqual(Expense.CATEGORIES[0][0], expense.category)
        self.assertEqual('foo', expense.description)
        self.assertEqual(date(2015, 12, 31), expense.date)
