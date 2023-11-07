import keyboard
from time import sleep
import sys, os

left = 0.0
right = 0.0

import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



while True:
    char = keyboard.read_key()  # Read keyboard	
    if char=='a':
        left=left-0.1
    if char=='s':
        left=left+0.1
    if char=='f':
        right=right-0.1
    if char=='d':
        right=right+0.1
    if char=='b':
        right = 0.0
        left = 0.0
    if char=='w':
        right = 0.5
        left = 0.5
    sleep(0.2)
    print(right, left)
    
    #dataKodet = data.encode()
    #sock.sendto(dataKodet, (host, port))

    
