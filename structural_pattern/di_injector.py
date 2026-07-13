from injector import Injector, inject

class Service:
    def __init__ (self):
        pass
    def do_service(self)->None:
        print("done service")


class Client:
    @inject
    def __init__(self, service:Service):
        self.service=service
    def avail_service(self)->None:
        self.service.do_service()


def main()->None:
    inject=Injector()
    client= inject.get(Client)
    client.avail_service()

if __name__=="__main__":
    main()
    print("done")
