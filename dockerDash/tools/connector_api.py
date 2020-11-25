import requests
class query_api:
    def __init__(self, head, host, port, url, params=None):
        self.head = head
        self.host = host
        self.port = port
        self.url = url
        self.params = params
    def __str__(self):
        return f"{self.host}:{self.port}\{self.url}"

    def queryGet(self):
        print(f'http://{self.host}:{self.port}{self.url}')
        url = f'http://{self.host}:{self.port}{self.url}'
        params = dict(
        )
        if self.params != None:
            params + self.params
        resp = requests.get(url=url, params=params)
        return resp

    def queryPost(self):
        url = f'http://{self.host}:{self.port}{self.url}'
        params = dict(
        )
        if self.params != None:
            params + self.params
        resp = requests.post(url=url, params=params)
        return resp

    def query(self):
        head = str(self.head).upper()
        if head == "POST":
            return self.queryPost().json()
        elif head == "GET":
            return self.queryGet().json()

    def status_code(self):
        head = str(self.head).upper()
        if  head == "POST":
            return self.queryPost().status_code
        elif  head == "GET":
            return self.queryGet().status_code
        else:
            print("Error: please select right head for api query")
            return False

'''
    Example how create simple API query
    head = "GET"
    host = "10.100.102.52"
    port = "2375"
    url = "/containers/json"
    query_api(head, host, port, url).query()
'''

def query_all_servers(head, url, params=None):
    result = []
    from servers.models import server
    for s in server.objects.all():
        result.append(query_api(head=head, host=s.host, port=s.api_port, url=url).query())
    return result

def resolve_host_by_id(host_id):
    #result = {"status": False, "data":None}
    from servers.models import server
    return server.objects.get(id=host_id)

# Classes
#====================
class networks_class:
    @staticmethod
    def print_all_networks_by_server_id(host_id):
        host = resolve_host_by_id(host_id)
        print(f"Host: {host}")
        return query_api(head='GET', host=host.host, port=host.api_port, url="/networks").query()

    @staticmethod
    def print_all_networks_from_all_servers():
        from servers.models import server as server_model
        all_networks= []
        for s in server_model.objects.all():
            if s.status == True:
                try:
                    all_networks.append({"server": f"{s.host}:{s.api_port}", "data": networks_class.print_all_networks_by_server_id(s.id)})
                except Exception as e:
                    print(f"Error: {e}")
        return all_networks
class images_class:
    images_url = "/images/json"

    @staticmethod
    def print_all_images():
        from tools.objects import image_object
        from hurry.filesize import size

        images = []

        api = query_all_servers(head="GET", url=images_class.images_url)
        for host in api:
            for image in host:
                images.append(image_object(Containers=image['Containers'], Created=image['Created'], Id=image['Id'], Labels=image['Labels'], ParentId=image['ParentId'], RepoDigests=image['RepoDigests'][0], RepoTags=image['RepoTags'][0], SharedSize=image['SharedSize'], Size=size(image['Size']), VirtualSize=size(image['VirtualSize'])))
        return images





