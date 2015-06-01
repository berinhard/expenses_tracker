# coding:utf-8
import json
from model_mommy import mommy

from django.core.urlresolvers import reverse
from django.test import TestCase

from src.expenses.models import Expense

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
