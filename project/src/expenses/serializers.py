# coding:utf-8
from rest_framework import serializers

from src.expenses.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    category_display = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    def get_category_display(self, obj):
        return obj.get_category_display()

    def get_date(self, obj):
        return obj.date.strftime('%d/%m/%Y')

    class Meta:
        model = Expense
        fields = ['id', 'value', 'category', 'date', 'description', 'category_display']
        read_only_fields = ['id', 'category_display']
