import socket
from time import sleep

from machine import ADC, Pin

SPEED = ADC(Pin(1, Pin.IN), atten=ADC.ATTN_11DB)
STEER = ADC(Pin(2, Pin.IN), atten=ADC.ATTN_11DB)

debug = True
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("192.168.4.1", 7913)

def getProcent(pot):
    return round(pot.read_uv()/1000/3027*100)

def getCmd(speed, steer):
    if steer <= 50:
        lspeed = speed-abs(50-steer)
        rspeed = speed
    else:
        lspeed = speed
        rspeed = speed-abs(50-steer)
    return f"{lspeed} {rspeed}"

while True:
    msg = getCmd(getProcent(SPEED), getProcent(STEER))
    #print(msg)
    sock.sendto(msg, server_addr)
    sleep(0.05)
