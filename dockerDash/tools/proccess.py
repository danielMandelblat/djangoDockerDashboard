interval = 1


def check_servers_status():
    import time
    from datetime import datetime
    while True:
        print(f"New process check started at: [{datetime.now()}]")
        from servers.models import server
        all_servers = server.objects.all()

        #Process 1 - check sevrers power status and expoerm information
        for server in all_servers:
            # Validate connectivity to the new server(Checking the port also)
            def test_connection_and_port(host, port):
                import socket

                try:
                    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    location = (host, port)

                    result_of_check = a_socket.connect_ex(location)

                    if result_of_check == 0:
                        status = 'Success'
                        server.status = True
                        a_socket.close()
                    else:
                        print(f"Critical Error: server [{server.host}:{server.api_port}] is not accessible")
                        status = 'Failed'
                        server.status = False
                except:
                    status = 'Failed'
                    server.status = False
                finally:
                    print(f"Testing - Host: {server.host} port: {server.api_port} status: [{status}]")
                    server.save()
            import threading
            threading.Thread(target=test_connection_and_port, args=(server.host, server.api_port)).start()

            # Query server and get server information
            def export_server_data_to_db():
                from servers.tools.connector_api import common_queries
                result = common_queries(server.host, server.api_port).print_server_info()

                server.Server_ID = result['ID']
                server.Containers = result['Containers']
                server.ContainersRunning = result['ContainersRunning']
                server.ContainersPaused = result['ContainersPaused']
                server.ContainersStopped = result['ContainersStopped']
                server.Images = result['Images']
                server.KernelVersion = result['KernelVersion']
                server.OperatingSystem = result['OperatingSystem']
                server.OSType = result['OSType']
                server.Architecture = result['Architecture']
                server.MemTotal = result['MemTotal']
                server.HostName = result['Name']
                server.ServerVersion = result['ServerVersion']

                server.save()
            export_server_data_to_db()
        # Process 2 - None
        time.sleep(interval)

def process_manager(run=False):
    import threading
    if run == True:
        print(f"Running process with interval of: [{interval}S]")
        threading.Thread(target=check_servers_status).start()


