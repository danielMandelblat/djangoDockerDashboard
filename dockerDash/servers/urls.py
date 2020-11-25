from django.urls import path, include
from servers.views import index, new, test

urlpatterns = [
    path('', index, name='index_servers'),
    path('new/', new, name='new_server'),
    path('test/', test)
]
