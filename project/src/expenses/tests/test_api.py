# coding:utf-8
import json
from model_mommy import mommy

from django.core.urlresolvers import reverse
from django.test import TestCase

from src.expenses.api import ListExpensesAPI
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
        mommy.make(Expense)

        qs = Expense.objects.all()

        self.assertEqual(list(qs), list(ListExpensesAPI.queryset))
        self.assertEqual(ExpenseSerializer, ListExpensesAPI.serializer_class)
