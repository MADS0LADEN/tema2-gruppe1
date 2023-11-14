import socket
import time

import pygame

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
        send(f"rmotor {speed}")
        send(f"lmotor {speed}")
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        send(f"rmotor {speed}")
        send(f"lmotor {speed}")
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        send(f"rmotor {int(speed/5)}")
        send(f"lmotor {int(speed/2)}")
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        send(f"rmotor {int(speed/2)}")
        send(f"lmotor {int(speed/5)}")
    if keys[pygame.K_e]:
        send("0")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()