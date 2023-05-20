import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server



class Request:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        
    def NewUser (Request, login, password):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    
            login_bytes = login[0].encode('utf-8')
            password_bytes = password[0].encode('utf-8')
            sendmessage = (str(login_bytes + password_bytes)[0]).encode('utf-8')
            s.connect((HOST, PORT))
            s.sendall((sendmessage))




