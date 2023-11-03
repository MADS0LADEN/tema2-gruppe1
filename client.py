import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("127.0.0.1", 7913)

while True:
    inp = input("Send besked: ").encode()
    sock.sendto(inp, server_addr)
    print(server_addr, inp.decode())