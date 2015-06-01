# coding:utf-8
import json
from model_mommy import mommy

from django.core.urlresolvers import reverse
from django.test import TestCase

from src.expenses.models import Expense
from src.expenses.serializers import ExpenseSerializer

class TestExpensesListApiMethod(TestCase):

    def setUp(self):
        self.url = reverse('expenses:list_expenses')

    def test_returns_expected_json(self):
        mommy.make(Expense)

        response = self.client.get(self.url)
        content = json.loads(response.content)

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(content))
        expected_keys = ['id', 'value', 'category', 'category_display', 'date', 'description']
        for key in expected_keys:
            self.assertIn(key, content[0])

    def test_ensure_generic_view_configuration(self):
        from src.expenses.api import ListExpensesAPI
        mommy.make(Expense)

        qs = Expense.objects.all()

        self.assertEqual(list(qs), list(ListExpensesAPI.queryset))
        self.assertEqual(ExpenseSerializer, ListExpensesAPI.serializer_class)


class TestExpenseResourceApiMethods(TestCase):

    def setUp(self):
        mommy.make(Expense, id=42)
        self.url = reverse('expenses:expense_detail', args=[42])

    def test_return_correct_object(self):
        response = self.client.get(self.url)
        content = json.loads(response.content)

        self.assertEqual(200, response.status_code)
        self.assertEqual(42, content['id'])

    def test_404_if_expense_does_not_exist(self):
        url = reverse('expenses:expense_detail', args=[1000])
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_ensure_generic_view_configuration(self):
        from src.expenses.api import ExpenseResourceAPI
        mommy.make(Expense)

        qs = Expense.objects.all()

        self.assertEqual(list(qs), list(ExpenseResourceAPI.queryset))
        self.assertEqual(ExpenseSerializer, ExpenseResourceAPI.serializer_class)
        self.assertEqual('expense_id', ExpenseResourceAPI.lookup_url_kwarg)

    def test_deletes_expense(self):
        self.assertTrue(Expense.objects.filter(id=42).exists())

        response = self.client.delete(self.url)

        self.assertEqual(204, response.status_code)
        self.assertFalse(Expense.objects.filter(id=42).exists())
