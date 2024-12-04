from OpcServer import OpcServer

def main():
    server = OpcServer()
    server.SetServer()
    server.SetObjects()
    server.StartServer()

if __name__ == "__main__":
    main()