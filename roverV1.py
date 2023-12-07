# -*- codOUTg: utf-8 -*-

# Dette program får har en
from machine import PWM, Pin

mOUT1 = Pin(16, Pin.OUT)
mOUT2 = Pin(13, Pin.OUT)
mEn1 = PWM(Pin(15, Pin.OUT), freq=100, duty_u16=0)
mEn2 = PWM(Pin(14, Pin.OUT), freq=100, duty_u16=0)


def duty(pwm, procent):
    duty_value = int(65535 / 100 * procent)
    pwm.duty_u16(duty_value)


def startup():
    duty(mEn1, 50)
    duty(mEn2, 50)
    mOUT1.value(1)
    mOUT2.value(1)


while True:
    startup()
