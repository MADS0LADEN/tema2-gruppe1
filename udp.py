import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 7913

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print(f"{addr}: {data.decode()}")