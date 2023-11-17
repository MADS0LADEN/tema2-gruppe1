# Dette program tager input fra et joystick som er koblet op til esp32eren.
# Den bruger ADC/analog to digital konverter.
# vi modtager input fra joystikket i form af volt der rangere fra 0 til 65500.
# Vi bruger så det input fra joystikket til at slukke og tænde lamper, efter hvilken retning stikket peger i mod

# funktionerne som jeg importere
from time import sleep

from machine import ADC, Pin

# xAxis og yAxis modtager input fra joystik armen
xAxis = ADC(Pin(1, Pin.IN), atten=ADC.ATTN_11DB)
yAxis = ADC(Pin(2, Pin.IN), atten=ADC.ATTN_11DB)
# button modtager inputtet fra når man trykker på knappen
button = Pin(3, Pin.IN, Pin.PULL_UP)
# de nedenstående pins sender strøm ud til de forskellige lamper
lampemid = Pin(41, Pin.OUT)
led_left = Pin(40, Pin.OUT)
led_right = Pin(13, Pin.OUT)
led_up = Pin(38, Pin.OUT)
led_down = Pin(12, Pin.OUT)


# While loopet core så længe programmet kører
while True:
    # xValue og yValue aflæser her joystikkets placering, og sender et signal tilbage i microvolt
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    # buttonStatus bliver lige med not pressed, fordi knappen som udgangspunkt ikke er trykket nede
    buttonvalue = button.value()
    buttonStatus = "not pressed"
    # her er alle værdierne af lamperne sat til nul, fordi der kun skal løbe strøm til dem, når de bliver
    # "aktiveret" af joystikket
    ledMid = lampemid.value(0)
    led_left.value(0)
    led_down.value(0)
    led_up.value(0)
    led_right.value(0)

    # hvis joystikket trykkes ned får den værdien pressed
    if buttonvalue == 0:
        buttonStatus = "pressed"
    # når knappen bliver trykket på lyser lampen
    if buttonStatus == "pressed":
        ledMid = lampemid.value(1)

    # får de forskellige lamper til at lyse alt efter hvilken x- og y-værdi der er på joystikket.
    if xValue <= 600:
        xStatus = "left"
        led_left.value(1)

    if xValue >= 60000:
        xStatus = "right"
        led_right.value(1)

    if yValue <= 600:
        yStatus = "up"
        led_up.value(1)

    if yValue >= 60000:
        yStatus = "down"
        led_down.value(1)

    print(f"x: {xValue}, y: {yValue}, button: {buttonStatus}")
    sleep(0.5)
