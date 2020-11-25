from django.urls import path
from services.views import service_server_update
urlpatterns = [
    path('admin/', service_server_update, name='service_server_update'),
]
