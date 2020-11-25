from django.shortcuts import redirect
import tools.proccess as process

# Create your views here.
def service_server_update(request):
    process.check_servers_status()
    return redirect('index_servers')