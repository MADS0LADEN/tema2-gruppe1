def parseSpeed(speed: str) -> int:
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
    
def execute(cmd, speed):
    if cmd == "forward":  forward(speed)
    if cmd == "backward": backward(speed)
    if cmd == "right":    right(speed)
    if cmd == "left":     left(speed)
