# coding:utf-8
from rest_framework.generics import ListAPIView, RetrieveAPIView

from src.expenses.serializers import ExpenseSerializer
from src.expenses.models import Expense


class ListExpensesAPI(ListAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


class ExpenseDetailAPI(RetrieveAPIView):
    serializer_class = ExpenseSerializer
    lookup_url_kwarg = 'expense_id'
    queryset = Expense.objects.all()
