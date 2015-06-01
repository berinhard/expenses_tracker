# coding:utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestIndexView(TestCase):

    def test_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')
