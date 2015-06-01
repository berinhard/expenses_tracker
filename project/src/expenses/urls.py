from django.conf.urls import patterns, url

def foo(request):
    pass

urlpatterns = patterns('',
    url(r'^list-expenses/$', foo, name="list_expenses")
)
