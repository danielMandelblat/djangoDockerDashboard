from django.shortcuts import render
from tools.connector_api import images_class

def index_images(request):
    data= {'images_from_hosts': images_class.print_all_images()}
    return render(request, 'images.html', data)

def new_image(request):
    return render(request, 'new_image.html')