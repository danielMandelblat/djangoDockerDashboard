from django.db import models
from django.core.exceptions import ValidationError
from servers.tools.connector_api import query_api

def now():
    from datetime import datetime
    return datetime.now()

class server(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    host = models.CharField(max_length=250, unique=True)

    install_type_choices = (
        ("new", "New server without nothing"),
        ("docker", "Only Docker installed"),
        ("api", "Running Docker server with enabled API"),
    )
    install = models.CharField(max_length=250, choices=install_type_choices)
    date_created = models.DateTimeField(default=now)
    date_updated = models.DateTimeField(default=now)
    status = models.BooleanField(default=False)

    SSH_username = models.CharField(max_length=250, null=True, blank=True, default='root')
    SSH_password = models.CharField(max_length=250, null=True, blank=True)
    SSH_port = models.PositiveIntegerField(null=True, blank=True, default=22)
    api_port = models.PositiveIntegerField(null=True, blank=True, default=2375)

    Server_ID = models.CharField(max_length=250, null=True, blank=True)
    Containers = models.CharField(max_length=250, null=True, blank=True)
    ContainersRunning = models.CharField(max_length=250, null=True, blank=True)
    ContainersPaused = models.CharField(max_length=250, null=True, blank=True)
    ContainersStopped = models.CharField(max_length=250, null=True, blank=True)
    Images = models.CharField(max_length=250, null=True, blank=True)
    KernelVersion = models.CharField(max_length=250, null=True, blank=True)
    OperatingSystem = models.CharField(max_length=250, null=True, blank=True)
    OSType = models.CharField(max_length=250, null=True, blank=True)
    Architecture = models.CharField(max_length=250, null=True, blank=True)
    MemTotal = models.CharField(max_length=250, null=True, blank=True)
    HostName = models.CharField(max_length=250, null=True, blank=True)
    ServerVersion = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.name

    def clean(self):
        # Validate connectivity to the new server(Checking the port also)
        def test_connection_and_port(host, port):
            import socket
            try:
                a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                location = (host, port)
                print(f"Testing - Host: {self.host} port: {self.api_port}")

                result_of_check = a_socket.connect_ex(location)
                if result_of_check == 0:
                    self.status = True
                    a_socket.close()
                else:
                    self.status = False

            except Exception as e:
                raise ValidationError(f"[{host}:{port}] is not available Error: [{e}]")

        test_connection_and_port(self.host, self.api_port)

        # Query server and get server inforamation
        from servers.tools.connector_api import common_queries
        result = common_queries("10.100.102.52", 2375).print_server_info()

        self.Server_ID = result['ID']
        self.Containers = result['Containers']
        self.ContainersRunning
        self.ContainersPaused
        self.ContainersStopped
        self.Images
        self.KernelVersion
        self.OperatingSystem
        self.OSType
        self.Architecture
        self.MemTotal
        self.HostName
        self.ServerVersion

