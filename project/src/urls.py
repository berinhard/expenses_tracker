# coding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'', include('src.expenses.urls', namespace='expenses')),
    url(r'^admin/', include(admin.site.urls)),
]
