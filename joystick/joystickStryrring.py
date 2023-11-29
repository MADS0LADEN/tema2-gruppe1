from time import sleep

from machine import ADC, Pin

# xAxis og yAxis modtager input fra joystik armen
xAxis = ADC(Pin(1, Pin.IN), atten=ADC.ATTN_11DB)
yAxis = ADC(Pin(2, Pin.IN), atten=ADC.ATTN_11DB)
# button modtager inputtet fra når man trykker på knappen
button = Pin(3, Pin.IN, Pin.PULL_UP)
xStatus = ""
yStatus = ""
forward = 0
right = 0
left = 0
back = 0
boost = 0
result = ""

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

basespeed = 65
while True:
    # xValue og yValue aflæser her joystikkets placering, og sender et signal tilbage i microvolt
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    # buttonStatus bliver lige med not pressed, fordi knappen som udgangspunkt ikke er trykket nede
    buttonvalue = button.value()
    buttonStatus = "not pressed"
    # hvis joystikket trykkes ned får den værdien pressed
    if buttonvalue == 0:
        buttonStatus = "pressed"
    # når knappen bliver trykket på lyser lampen
    if buttonStatus == "pressed":
        pass

    # får de forskellige lamper til at lyse alt efter hvilken x- og y-værdi der er på joystikket.
    if xValue <= 600:
        xStatus = "left"

    if xValue >= 60000:
        xStatus = "right"

    if yValue <= 600:
        yStatus = "up"

    if yValue >= 60000:
        yStatus = "down"

    if 10000 <= xValue <= 50000:
        xStatus = "neutral"

    if 10000 <= yValue <= 50000:
        yStatus = "neutral"

    # straight ahead: no turning
    if yStatus == "up" and xStatus == "neutral":
        forward = 65 + boost
        if 40 <= forward < 97:
            boost += 2
        result = str(forward) + " " + str(forward)
    # neutral: the joystick is in the middle and every value is 0
    if yStatus == "neutral" and xStatus == "neutral":
        left = 0
        right = 0
        boost = 0
        result = str(left) + " " + str(right)
    # Direct left turn: the rover stops moving forward and swings left
    if yStatus == "neutral" and xStatus == "left":
        left = 0
        right = 20
        boost= 0
        result = str(left) + " " + str(right)
    # Direct right turn: the rover stops moving forward and swings right
    if yStatus == "neutral" and xStatus == "right":
        left = 20
        right = 0
        boost = 0
        result = str(left) + " " + str(right)
    # Left swing: the rover turns left while moving forward
    if yStatus == "up" and xStatus == "left":
        left = basespeed
        right = basespeed + 15
        boost = 10
        result = str(left) + " " + str(right)
    # Right swing: the rover turns right while moving forward
    if yStatus == "up" and xStatus == "right":
        left = basespeed + 15
        right = basespeed
        boost = 10
        result = str(left) + " " + str(right)

    if yStatus == "down" and xStatus == "neutral":
        back = -35
        result = str(back) + " " + str(back)
        
    sleep(0.2)
    
    inp = result.encode()
    if not debug and len(inp) == 0:
        inp = "NAN".encode()
    try:
        sock.sendto(inp, server_addr)
        print(inp)
        print(server_addr, len(inp), inp.decode())
    except OSError:
        print("Not connected to Rover")
