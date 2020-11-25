from django.forms import ModelForm
from servers.models import server

class new_server_form(ModelForm):

    class Meta:
        model = server
        fields = [
            'name', 'host', 'api_port'
        ]