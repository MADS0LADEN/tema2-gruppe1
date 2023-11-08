import socket

debug = True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
enpoint = input("Hvilken endhed vil du snakke med?\nESP / LOCAL?\n")
if enpoint.lower() == "esp":
    server_addr = ("192.168.4.1", 7913)
else:
    server_addr = ("127.0.0.1", 7913)

while True:
    inp = input("Send besked: ").encode()
    if not debug and len(inp) == 0:
        inp = "NAN".encode()
    try:
        sock.sendto(inp, server_addr)
        print(server_addr, len(inp), inp.decode())
    except OSError:
        print("Not connected to Rover")