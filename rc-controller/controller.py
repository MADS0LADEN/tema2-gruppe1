import socket
from time import sleep

from machine import ADC, Pin

SPEED = ADC(Pin(1, Pin.IN), atten=ADC.ATTN_11DB)
STEER = ADC(Pin(2, Pin.IN), atten=ADC.ATTN_11DB)

debug = True
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("192.168.4.1", 7913)


def getProcent(pot):
    return round(pot.read_uv() / 1000 / 3027 * 100)


def getCmd(speed, steer):
    if speed < 11:
        speed = -abs(11 - speed) * 2
    else:
        speed = int(((speed - 11) / (23 - 11)) * 100)
    trim = round(speed - abs(50 - steer) / 3)
    if steer <= 50:
        rspeed = trim
        lspeed = speed
    else:
        rspeed = speed
        lspeed = trim
    return f"{lspeed} {rspeed}"


while True:
    msg = getCmd(getProcent(SPEED), getProcent(STEER))
    # print(msg)
    sock.sendto(msg, server_addr)
    sleep(0.05)
