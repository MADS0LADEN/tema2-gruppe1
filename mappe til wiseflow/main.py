import socket

import driver

debug = True
platform = None

UDP_IP = "0.0.0.0"
UDP_PORT = 7913

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
try:
    import network

    platform = "ESP"
    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.config(ssid="RoverNumber1", password="qwerty123456", authmode=3, max_clients=1)
    ap.active(True)
    print("Send packets to this IP:", ap.ifconfig()[2]) # Show IP
except Exception as e:
    platform = "PC"
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(e, "= not on ESP, use this IP if external", ip, "otherwise use localhost")

while True:
    data, addr = sock.recvfrom(32)
    data = data.decode().split(" ")
    size = len(data)
    if debug:
        print(f"{addr} bytes={size}: {data}")
    if size == 1:
        if data[0] == "0":
            driver.stop()
        elif data[0] != "0":
            freq = 0
            try:
                freq = abs(int(data[0]))
            except ValueError:
                continue
    if size == 2:
        cmd, speed = data
        if platform == "ESP":
            driver.execute(cmd, speed)
