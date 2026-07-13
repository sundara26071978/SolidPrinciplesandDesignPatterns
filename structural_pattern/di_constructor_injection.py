class Service:
    def do_service(self) -> None :
        print("Done service")

class Client:
    def __init__(self, service: Service):
        self.service= service
    
    def avail_service(self)->None:
        self.service.do_service()



def main()-> None :
    service= Service()
    client=Client(service)
    client.avail_service()

if __name__ =="__main__":
    main()

