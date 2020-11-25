from django.urls import path
from networks.views import index, new_network
urlpatterns = [
    path('', index, name='index_networks'),
    path('new_network', new_network, name='new_network'),
]
