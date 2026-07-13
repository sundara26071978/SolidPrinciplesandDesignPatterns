class Service:
    def do_service(self)->None:
        print("done service")

class Client:
    def avail_service(self, service : Service)->None:
        service.do_service()

def main() -> None:
    service= Service()
    client=Client()
    client.avail_service(service)


if __name__=="__main__":
    main()
    print("done")