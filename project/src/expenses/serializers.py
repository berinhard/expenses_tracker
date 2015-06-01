# coding:utf-8
from rest_framework import serializers

from django.core.urlresolvers import reverse

from src.expenses.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    category_display = serializers.SerializerMethodField()
    resource_url = serializers.SerializerMethodField()

    def get_category_display(self, obj):
        return obj.get_category_display()

    def get_resource_url(self, obj):
        return reverse('expenses:expense_detail', args=[obj.id])

    class Meta:
        model = Expense
        fields = ['id', 'value', 'category', 'date', 'description', 'category_display', 'resource_url']
        read_only_fields = ['id', 'category_display', 'resource_url']
