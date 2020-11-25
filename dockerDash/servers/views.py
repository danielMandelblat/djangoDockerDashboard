from django.shortcuts import render, redirect
from servers.forms import new_server_form
from django.contrib import messages
from servers.models import server

def index(request):
    data={}
    data['servers'] = server.objects.all()
    return render(request, 'servers.html', data)

def new(request):
    form = new_server_form(request.POST or None)
    if form.is_valid():
        #Save form data to DB
        form.save(commit=True)

        #Create var with our new server object
        server_object = server.objects.get(host=form.cleaned_data['host'])

        #Build the successfully message for user
        messages.success(request, f"Server {request.POST['host']} added successfully | Docker server ID: [{server_object.Server_ID}]")

        #Clean all form fields
        form = new_server_form()

    data = {"form":form}
    return render(request, 'new.html', data)

def test(request):
    from servers.tools.connector_api import query_all_servers
    query_all_servers(head="GET", url='/containers/json', params="")
    return redirect(index)