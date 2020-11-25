from django.urls import path
from images.views import index_images, new_image

urlpatterns = [
    path('', index_images, name='index_images'),
    path('new_image/', new_image, name='new_image'),

]