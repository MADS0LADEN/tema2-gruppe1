import socket
import time

import pygame

DELAY_NS = 50_000_000


class delay:
    def __init__(self, value) -> None:
        self.value = value
        self.delay_ns = DELAY_NS
        self.time_ns = time.time_ns()

    def __repr__(self) -> int:
        return self.value

    def set(self, value):
        now = time.time_ns()
        if now - self.time_ns >= self.delay_ns:
            self = value
            print(self.var, value)
            self.time_ns = time.time_ns()

    def get(self):
        return self

    def getDelay(self):
        return self.delay_ns


# socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
endpoint = ("192.168.4.1", 7913)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


def send(msg):
    if len(msg) != 0:
        sock.sendto(msg.encode(), endpoint)
        print(time.time(), msg)
    else:
        send("0")


speed = 100
trim_offset = 0
turn = 10


def goStraight(speed):
    leftSpeed = abs(speed)
    rightSpeed = abs(speed)
    if trim_offset < 0:
        leftSpeed -= abs(trim_offset)
    else:
        rightSpeed -= abs(trim_offset)
    invert = "-" if speed < 0 else ""
    send(f"{invert}{leftSpeed} {invert}{rightSpeed}")


last_execution = 0


def delayOffset(var):
    global last_execution, trim_offset
    curr_time = time.time_ns()
    if curr_time - last_execution >= DELAY_NS:
        trim_offset = var
        print(trim_offset)
        last_execution = time.time_ns()


def changeSpeed(var):
    global last_execution, speed
    curr_time = time.time_ns()
    if curr_time - last_execution >= DELAY_NS:
        speed = var
        print(speed)
        last_execution = time.time_ns()


def changeTurn(var):
    global last_execution, turn
    curr_time = time.time_ns()
    if curr_time - last_execution >= DELAY_NS:
        turn = var
        print(turn)
        last_execution = time.time_ns()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        goStraight(speed)
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        goStraight(int(f"-{speed}"))
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        send(f"{int(speed-turn)} {int(speed)}")
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        send(f"{int(speed)} {int(speed-turn)}")
    if keys[pygame.K_e]:
        delayOffset(trim_offset + 1)
    if keys[pygame.K_q]:
        delayOffset(trim_offset - 1)
    if keys[pygame.K_UP]:
        changeSpeed(speed + 1)
    if keys[pygame.K_DOWN]:
        changeSpeed(speed - 1)
    if keys[pygame.K_LEFT]:
        changeTurn(turn - 1)
    if keys[pygame.K_RIGHT]:
        changeTurn(turn + 1)
    if keys[pygame.K_SPACE]:
        send("0")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(25) / 1000

pygame.quit()
