import time
from turtle import pd
from opcua import Server
import opcua

class OpcServer:
    def __init__(self):

        self._url = "opc.tcp://localhost:4841/freeopcua/server/"

        self._server = Server()
        self._addspace = None
        
    def SetServer(self):
        self._server.set_endpoint(self._url)

        # Setup our own namespace, not really necessary but should be as informative as possible
        name = "OPCUA_SIMULATION_SERVER"
        self._addspace = self._server.register_namespace(name)

    # def ReadCSV(self):
    #     df = pd.read_csv("michal.csv", usecols=[
    #                                                                     'X-coordinate',
    #                                                                     'Y-coordinate',
    #                                                                     'Heading'
    #                                                                     ],
    #                                                                 engine='python')
        

    def SetObjects(self):
        objects = self._server.get_objects_node()
        CoBotAGV_Now = objects.add_folder(self._addspace, "CoBotAGV_Now")
        FN_ID_6000 = CoBotAGV_Now.add_object(self._addspace, "FN_ID_6000")
        nns = FN_ID_6000.add_folder(self._addspace, "[NNS] - Natural Navigation Signals")
        var1 = nns.add_variable(self._addspace, "Heading", 0.0, datatype=opcua.ua.NodeId(opcua.ua.ObjectIds.Float))
        var2 = nns.add_variable(self._addspace, "X-coordinate", 0.0, datatype=opcua.ua.NodeId(opcua.ua.ObjectIds.Float))
        var3 = nns.add_variable(self._addspace, "Y-coordinate", 0.0, datatype=opcua.ua.NodeId(opcua.ua.ObjectIds.Float))
        var4 = nns.add_variable(self._addspace, "Current segment", 0.0, datatype=opcua.ua.NodeId(opcua.ua.ObjectIds.Float))
        var1.set_writable()
        var2.set_writable()
        var3.set_writable()
        var4.set_writable()
        

    def StartServer(self):
        self._server.start()
        try:
            while True:
                time.sleep(0.2)
        finally:
            # Close the connection, cleanup
            self._server.stop()
            print("Server stopped")

    # def HandleWritingValues(self):
    #     FinishFlag = False
    #     i = 0
    #     while not FinishFlag:
            



    #         time.sleep(0.1)





