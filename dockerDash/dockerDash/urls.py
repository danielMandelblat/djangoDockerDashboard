from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import networks.urls as networks_url
import servers.urls as servers_urls
import services.urls as services
import images.urls as images
urlpatterns = [
    path('admin/', admin.site.urls),
    path('servers/', include(servers_urls)),
    path('networks/', include(networks_url)),
    path('services/', include(services)),
    path('images/', include(images)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
