import socket
import threading
import sys
import time

host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
PORT='9999'
LISTENERLIMIT=1

def main():
    server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server.bind((host_name,PORT))
    except:
        print(f"Connection not established to host {HOST} AND PORT {PORT}")
    server.listen(LISTENERLIMIT)

    while True:
        conn, address = server.accept()
        print(f"Connection established to {address[0]}")

    client = (conn.recv(1024)).decode()
    print(client + ' has connected.')
 
conn.send(name.encode())

    while True:
        message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
if __name__== '__main__':
    main()






# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
# PORT = 9999 # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)