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
        resp = None

        print(f'http://{self.host}:{self.port}{self.url}')
        url = f'http://{self.host}:{self.port}{self.url}'
        params = dict(
        )
        if self.params != None:
            params + self.params

        try:
            resp = requests.get(url=url, params=params).json()
        except  Exception as e:
            print("Error: {e}")
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
        try:
            head = str(self.head).upper()
            if head == "POST":
                return self.queryPost().json()
            elif head == "GET":
                return self.queryGet()
        except:
            return [False,]
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

class common_queries:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def print_server_info(self):
        return query_api(head="get", host=self.host, port=self.port, url='/info').query()

