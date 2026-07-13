class Service:
    def do_service(self)-> None:
        print("done service")

class Client:
    def __init__(self):
        self.service=None

    def set_service(self, service :Service)->None:
        self.service=service
    
    def avail_service(self)-> None:
        self.service.do_service()

def main()->None:
    service=Service()
    client=Client()
    client.set_service(service)
    client.avail_service()
    print("done")

if __name__=="__main__":
    main()
    
