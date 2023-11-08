from machine import PWM, Pin

FREQ = 200
DUTY = 0

DIR_M1 = Pin(16, Pin.OUT)
DIR_M2 = Pin(13, Pin.OUT)
PWM_M1 = PWM(Pin(15, Pin.OUT), freq=FREQ, duty_u16=DUTY)
PWM_M2 = PWM(Pin(14, Pin.OUT), freq=FREQ, duty_u16=DUTY)

def calcDuty(percentage):
    return int(65535/100 * percentage)

def runM1(DIR, speed):
    DIR_M1.value(DIR)
    PWM_M1.duty_u16(calcDuty(speed))

def runM2(DIR, speed):
    DIR_M2.value(DIR)
    PWM_M2.duty_u16(calcDuty(speed))

def parseSpeed(speed) -> int:
    speed = str(speed)
    if speed.isdigit():
        speed = int(speed)
        if speed <= 100:
            return speed
        elif speed > 100:
            return 100
    else:
        return 0

def forward(speed):
    print("for", parseSpeed(speed))
def backward(speed):
    print("back", parseSpeed(speed))
def right(speed):
    print("r", parseSpeed(speed))
def left(speed):
    print("l", parseSpeed(speed))
def rMotor(speed):
    #print("rMotor", parseSpeed(speed))
    runM1(0, parseSpeed(speed))
def lMotor(speed):
    #print("lMotor", parseSpeed(speed))  
    runM2(1, parseSpeed(speed))

def stop():
    rMotor(0)
    lMotor(0)

def execute(cmd, speed):
    if cmd == "forward":  forward(speed)
    if cmd == "backward": backward(speed)
    if cmd == "right":    right(speed)
    if cmd == "left":     left(speed)
    if cmd == "rmotor":   rMotor(speed)
    if cmd == "lmotor":   lMotor(speed)
