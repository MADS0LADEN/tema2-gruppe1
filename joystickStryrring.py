from machine import Pin, ADC
from time import sleep
import socket
#xAxis og yAxis modtager input fra joystik armen
xAxis = ADC(Pin(1, Pin.IN), atten=ADC.ATTN_11DB)
yAxis = ADC(Pin(2, Pin.IN), atten=ADC.ATTN_11DB)
#button modtager inputtet fra når man trykker på knappen
button = Pin(3,Pin.IN, Pin.PULL_UP)
xStatus=""
yStatus=""
forward = 0
right = 0
left = 0
back = 0
result = ""

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
    #xValue og yValue aflæser her joystikkets placering, og sender et signal tilbage i microvolt
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    #buttonStatus bliver lige med not pressed, fordi knappen som udgangspunkt ikke er trykket nede
    buttonvalue= button.value()                                 
    buttonStatus= "not pressed"
    #hvis joystikket trykkes ned får den værdien pressed
    if buttonvalue == 0:
        buttonStatus = "pressed"
    #når knappen bliver trykket på lyser lampen
    if buttonStatus == "pressed":
        pass
        
    #får de forskellige lamper til at lyse alt efter hvilken x- og y-værdi der er på joystikket.    
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
        
    
    #print(f"x: {xValue}, y: {yValue}, button: {buttonStatus}")
    #print(f"xstatus: {xStatus} ystatus: {yStatus}")
    
    #straight ahead: no turning
    if yStatus == "up" and xStatus == "neutral":
        left = 0
        right = 0
        back = 0
        if forward == 0:
            forward = 40
        elif 40 <= forward < 100:
            forward += 5
    #neutral: the joystick is in the middle and every value is 0        
    if yStatus == "neutral" and xStatus == "neutral":
        forward = 0
        left = 0
        right = 0
        back = 0
    #Direct left turn: the rover stops moving forward and swings left 
    if yStatus == "neutral" and xStatus == "left":
        forward = 0
        left = 0
        right = 20
        back = 0
    #Direct right turn: the rover stops moving forward and swings right
    if yStatus == "neutral" and xStatus == "right":
        forward = 0
        left = 20
        right = 0
        back = 0
    #Left swing: the rover turns left while moving forward
    if yStatus == "up" and xStatus == "left":
        forward = 0
        left = 30
        right = 50
        back = 0
    #Right swing: the rover turns right while moving forward
    if yStatus == "up" and xStatus == "right":
        forward = 0
        left = 50
        right = 30
        back = 0
    
    if yStatus == "down" and xStatus == "neutral":
        back = 30
        
      
    #print(forward, left, right, back)
    sleep(0.5)
    li = [forward, left, right, back]
    
    if forward > left and forward > right:
        result = f"forward {forward}"
    elif forward < left or forward < right:
        result = f"lmotor {left} rmotor {right}"
    elif forward <= 0 and left <= 0 and right <= 0:
        result = f"forward {forward}"s
        
    #print(result)
    
    inp =result.encode()
    if not debug and len(inp) == 0:
        inp = "NAN".encode()
    try:
        sock.sendto(inp, server_addr)
        print(server_addr, len(inp), inp.decode())
    except OSError:
        print("Not connected to Rover")
