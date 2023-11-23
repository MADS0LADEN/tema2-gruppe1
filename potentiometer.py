from machine import Pin, ADC
from time import sleep
import socket
import math

po1 = ADC(Pin(3, Pin.IN), atten=ADC.ATTN_11DB)
po2 = ADC(Pin(4, Pin.IN), atten=ADC.ATTN_11DB)

en1 = Pin(1, Pin.OUT)
en2 = Pin(2, Pin.OUT)
button = Pin(5,Pin.IN, Pin.PULL_UP)

pressCount = 0

debug = True
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
enpoint = input("Hvilken endhed vil du snakke med?\nESP / LOCAL?\n")
if enpoint.lower() == "esp":
    server_addr = ("192.168.4.1", 7913)
elif enpoint.lower() == "mads":
    server_addr = ("192.168.1.130", 7913)
else:
    server_addr = ("127.0.0.1", 7913)


def toProcent(data):
    return math.floor(data/65536*100)
    
while True:
                                     
    buttonStatus= "not pressed"
    
    if button.value() == 0:
         pressCount += 1
         
    if pressCount == 1:
        buttonStatus = "pressed"
    if pressCount == 2:
        pressCount = 0
             
    print(buttonStatus)
    
    en1.value(1)
    en2.value(1)
    
    po1Val=po1.read_u16()
    po2Val=po2.read_u16()
    
    print(po1Val,po2Val)
    sleep(0.2)
    if buttonStatus =="not pressed":
        result = str(toProcent(po1Val)) + " " + str(toProcent(po2Val))
    elif buttonStatus == "pressed":
        result = str(-toProcent(po1Val)) + " " + str(-toProcent(po2Val))

    inp =result.encode()
    if not debug and len(inp) == 0:
        inp = "NAN".encode()
    try:
        sock.sendto(inp, server_addr)
        print(inp)
        print(server_addr, len(inp), inp.decode())
    except OSError:
        print("Not connected to Rover")