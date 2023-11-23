from machine import PWM, Pin

FREQ = 100
DUTY = 0

DIR_M1 = Pin(16, Pin.OUT)
DIR_M2 = Pin(13, Pin.OUT)
PWM_M1 = PWM(Pin(15, Pin.OUT), freq=FREQ, duty_u16=DUTY)
PWM_M2 = PWM(Pin(14, Pin.OUT), freq=FREQ, duty_u16=DUTY)


def calcDuty(percentage):
    return int(65535 / 100 * abs(percentage))


def parseSpeed(speed) -> int:
    try:
        float(speed)
        return int(speed)
    except ValueError:
        return 0


def setFreq(freq):
    freq = abs(round(float(freq)))
    freq = freq if freq > 10 else 10
    PWM_M1.freq(freq)
    PWM_M2.freq(freq)


def runM1(DIR, speed: int):
    DIR = DIR if speed > 0 else (not DIR)
    DIR_M1.value(DIR)
    PWM_M1.duty_u16(calcDuty(speed))


def runM2(DIR, speed: int):
    DIR = DIR if speed > 0 else (not DIR)
    DIR_M2.value(DIR)
    PWM_M2.duty_u16(calcDuty(speed))


def rMotor(speed):
    runM1(0, parseSpeed(speed))


def lMotor(speed):
    runM2(0, parseSpeed(speed))


def stop():
    rMotor(0)
    lMotor(0)


def execute(leftMotor, rightMotor):
    lMotor(leftMotor)
    rMotor(rightMotor)
