from machine import Pin, ADC
from time import sleep

po1 = ADC(Pin(3, Pin.IN), atten=ADC.ATTN_11DB)
po2 = ADC(Pin(4, Pin.IN), atten=ADC.ATTN_11DB)

en1 = Pin(1, Pin.OUT)
en2 = Pin(2, Pin.OUT)

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

while True:
    en1.value(1)
    en2.value(1)
    
    po1Val=po1.read_u16()
    po2Val=po2.read_u16()
    
    print(po1Val,po2Val)
    sleep(0.2)
    
    #Venstre motor styrring
    if po1Val <= 5000:
        left = 90
        lResult = "left" + str(left) 
    if 5001 <= po1Val <= 10000:
        left = 85
        lResult = "left" + str(left)
    if 10001 <= po1Val <= 15000:
        left = 80
        lResult = "left" + str(left)
    if 15001 <= po1Val <= 20000:
        left = 75
        lResult = "left" + str(left)
    if 20001 <= po1Val <= 25001:
        left = 70
        lResult = "left" + str(left)
    if 25001 <= po1Val <= 30000:
        left = 65
        lResult = "left" + str(left)
    if 30001 <= po1Val <= 35001:
        left = 60
        lResult = "left" + str(left)
    if 35001 <= po1Val <= 40000:
        left = 55
        lResult = "left" + str(left)
    if 40001 <= po1Val <= 45000:
        left = 50
        lResult = "left" + str(left)
    if 45001 <= po1Val <= 50000:
        left = 45
        lResult = "left" + str(left)
    if 50001 <= po1Val <= 55000:
        left = 20
        lResult = "left" + str(left)
    if 55001 <= po1Val:
        left = 0
        lResult = "left" + str(left)
        
        
    #Højre motor styrring
    if po2Val <= 5000:
        left = 90
        rResult = "right" + str(left) 
    if 5001 <= po2Val <= 10000:
        left = 85
        rResult = "right" + str(left)
    if 10001 <= po2Val <= 15000:
        left = 80
        rResult = "right" + str(left)
    if 15001 <= po2Val <= 20000:
        left = 75
        rResult = "right" + str(left)
    if 20001 <= po2Val <= 25001:
        left = 70
        rResult = "right" + str(left)
    if 25001 <= po2Val <= 30000:
        left = 65
        rResult = "right" + str(left)
    if 30001 <= po2Val <= 35001:
        left = 60
        rResult = "right" + str(left)
    if 35001 <= po2Val <= 40000:
        left = 55
        rResult = "right" + str(left)
    if 40001 <= po2Val <= 45000:
        left = 50
        rResult = "right" + str(left)
    if 45001 <= po2Val <= 50000:
        left = 45
        rResult = "right" + str(left)
    if 50001 <= po2Val <= 55000:
        left = 20
        rResult = "right" + str(left)
    if 55001 <= po2Val:
        left = 0
        rResult = "right" + str(left)
    print(lResult, rResult) 
'''       
    print(lResult, rResult)
    inp =result.encode()
    if not debug and len(inp) == 0:
        inp = "NAN".encode()
    try:
        sock.sendto(inp, server_addr)
        print(inp)
        print(server_addr, len(inp), inp.decode())
    except OSError:
        print("Not connected to Rover")
'''