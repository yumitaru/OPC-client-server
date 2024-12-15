import time
import pandas as pd
from opcua import Client
import opcua

class OPCClient:
    def __init__(self):
        self._url = "opc.tcp://localhost:4841/freeopcua/server/"
        self._client = Client(self._url)
        self._client.connect()
        self._nodeId = "ns=2;i="
        self._tab = [4,5,6,7,8]
        self._tab2 = ['X-coordinate','Y-coordinate', 'Heading', 'Current segment','Battery cell voltage']
        self._NNS = None
        self._frame6000 = None

    def HandleWriting(self):

        df = pd.read_csv("initial_data.csv", usecols=[
                                                                'X-coordinate',
                                                                'Y-coordinate',
                                                                'Heading',
                                                                'Current segment',
                                                                'Battery cell voltage'
                                                                ],
                                                            engine='python')
        time.sleep(5)
        
        it = 0
        while True:

            for i in self._tab:
                self.frame6000 = self._client.get_node("ns=2;i=" + str(i))
                value = self.frame6000.get_value()
                
                input = opcua.ua.DataValue(opcua.ua.Variant(float(df[self._tab2[i-4]][it]), opcua.ua.VariantType.Float))
                self.frame6000.set_value(input)
                print(value)
            it +=1
            time.sleep(2)
        