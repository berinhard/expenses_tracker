from django.conf.urls import patterns, url

from src.expenses.api import *


urlpatterns = patterns('',
    url(r'^list-expenses/$', ListExpensesAPI.as_view(), name="list_expenses")
)
