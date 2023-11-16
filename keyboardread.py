from time import sleep

import keyboard

left = 0.0
right = 0.0

import socket

debug = True
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
enpoint = input("Hvilken endhed vil du snakke med?\nESP / LOCAL?\n")
if enpoint.lower() == "esp":
    server_addr = ("192.168.4.1", 7913)
elif enpoint.lower() == "mads":
    server_addr = ("192.168.1.130", 7913)
else:
    server_addr = ("127.0.0.1", 7913)
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

baseSpeed = 30
speedL = baseSpeed
speedR = baseSpeed
while True:    
    char = keyboard.read_key()  # Read keyboard	
    result = "forward 0"
    if char=='a':
        speedR = speedR - 10
        speedL = baseSpeed
        result = "left " + str(speedR)
    if char=='s':
        left=left+0.1
        result = ("-"+baseSpeed, "-"+baseSpeed)
    if char=='f':
        right=right-0.1
    if char=='d':
        speedL = speedL - 10
        speedR = baseSpeed
        result = "right " + str(speedL)
    if char=='b':
        right = 0.0
        left = 0.0
    if char=='w':
        speedL = baseSpeed
        speedR = baseSpeed
        result = str(baseSpeed, baseSpeed)
    if char == 'e':
        result = "0"
    sleep(0.2)
    print(right, left)
    #dataKodet = data.encode()
    #sock.sendto(dataKodet, (host, port))
    inp =result.encode()
    if not debug and len(inp) == 0:
        inp = "NAN".encode()
    try:
        sock.sendto(inp, server_addr)
        print(server_addr, len(inp), inp.decode())
    except OSError:
        print("Not connected to Rover")