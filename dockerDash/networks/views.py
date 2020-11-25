from django.shortcuts import render, redirect

def index(request):
    from tools.connector_api import networks_class
    data = {'networks_servers': networks_class.print_all_networks_from_all_servers()}
    return render(request, 'networks.html', data)

def new_network(request):
    return render(request, 'new_network.html')

