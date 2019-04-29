from mprpc import RPCClient
import time

class CVPChatClient: 
    Client = RPCClient('127.0.0.1', 20181)

    while(True):
        Client.call('SendMessage', "Hello")
        Client.call('SendMessage', "JAM")
        Client.call('SendMessage', "x3")

        print(Client.call('GetRecentMessage'))
        time.sleep(1)