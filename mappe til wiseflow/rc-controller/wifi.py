import sys
import time
import network

wifi = network.WLAN(network.STA_IF)

if not wifi.isconnected():
    wifi.active(True)
    try:
        wifi.config(dhcp_hostname="RC Controller")
        wifi.connect("RoverNumber1", "qwerty123456")
    except Exception as err:
        wifi.active(False)
        print("Error:", err)
        sys.exit()
    print("Connecting", end="")
    n = 0
    while not wifi.isconnected():
        print(".", end="")
        time.sleep(1)
        n += 1
        if n == 60:
            break
    if n == 60:
        wifi.active(False)
        print("\nGiving up! Not connected!")
    else:
        print("\nNow connected with IP: ", wifi.ifconfig()[0])

