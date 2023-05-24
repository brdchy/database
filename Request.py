from msilib.schema import tables
import socket
from urllib import response

class Request:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def new_user(self, login, password):
        data = f"NewUser?{login}:{password}"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        print(response.decode('utf-8'))
        return str(response.decode('utf-8'))

    def message(self, message):
        data = f"{message}"
        self.sock.send(data.encode('utf-8'))

    def entrance(self, login, password):
        data = f"Entrance?{login}:{password}"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        print( response.decode('utf-8'))
        return str(response.decode('utf-8'))

    def admin_entrance(self, login, password):
        data = f"Admin?{login}:{password}"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        print( response.decode('utf-8'))
        return str(response.decode('utf-8'))

    def new_booking(self, name, phone, table, time, notes):
        data = f"NewBooking?{name},{phone},{table},{time},{notes}"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        book = str(response.decode('utf-8'))
        return book

    def UnloadUsers(self):
        data = "UnloadUsers?"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        users = str(response.decode('utf-8'))
        user_list = users.split('\n')
        return user_list
    
        #print(response.decode('utf-8'))

    def UnloadTables(self):
        data = "UnloadTables?"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        tables = str(response.decode('utf-8'))
        table_list = tables.split('\n')
        return table_list
    
    def DeleteUser(self, login):
        data = f"DeleteUser?{login}"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        print(response.decode('utf-8'))

    def DeleatUser(self, login):
        data = f"DeleatUser?{login}"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        print(response.decode('utf-8'))

    def close(self):
        self.sock.close()