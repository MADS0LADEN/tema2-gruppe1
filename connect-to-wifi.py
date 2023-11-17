# -*- coding: utf-8 -*-

import sys
import time

import network

sta_if = network.WLAN(network.STA_IF)

if not sta_if.isconnected():
    sta_if.active(True)
    try:
        sta_if.config(dhcp_hostname="My ProS3")
        sta_if.connect("ITLab", "MaaGodt*7913")
    except Exception as err:
        sta_if.active(False)
        print("Error:", err)
        sys.exit()
    print("Connecting", end="")
    n = 0
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(1)
        n += 1
        if n == 60:
            break
    if n == 60:
        sta_if.active(False)
        print("\nGiving up! Not connected!")
    else:
        print("\nNow connected with IP: ", sta_if.ifconfig()[0])
print(sta_if.ifconfig()[0])
