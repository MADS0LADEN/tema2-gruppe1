import socket

import driver

UDP_IP = "0.0.0.0"
UDP_PORT = 7913

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

try:
    import network

    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.config(ssid="RoverNumber1")
    ap.config(password="qwerty123456")
    ap.config(max_clients=1)
    ap.active(True)
    print(ap.ifconfig()[2]) # Show IP
except:
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("Not running on ESP, use this IP if external", ip, "otherwise use localhost")

while True:
    data, addr = sock.recvfrom(1024)
    cmd, speed = data.decode().split(" ")
    driver.execute(cmd, speed)
    print(f"{addr}: {data}")
