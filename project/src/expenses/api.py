# coding:utf-8
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework import mixins

from src.expenses.serializers import ExpenseSerializer
from src.expenses.models import Expense


class ListExpensesAPI(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


class ExpenseResourceAPI(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    serializer_class = ExpenseSerializer
    lookup_url_kwarg = 'expense_id'
    queryset = Expense.objects.all()

    def get(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.destroy(*args, **kwargs)
