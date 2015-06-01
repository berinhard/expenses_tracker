from django.conf.urls import patterns, url

from src.expenses.api import *


urlpatterns = patterns('',
    url(r'^expenses/$', ListExpensesAPI.as_view(), name="list_expenses"),
    url(r'^expenses/(?P<expense_id>\d+)/$', ExpenseDetailAPI.as_view(), name='expense_detail'),
)
