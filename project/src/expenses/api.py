# coding:utf-8
from rest_framework.generics import ListAPIView

from src.expenses.serializers import ExpenseSerializer
from src.expenses.models import Expense


class ListExpensesAPI(ListAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
