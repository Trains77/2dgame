import platform
import colored
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
pygame.init()
from time import sleep
from colored import fore, back, style
import math
import random
import credits
from shared import size, GameName, gravity, fps, background_color, BLACK, RED, GREEN, BLUE, WHITE, GRAY, player_color, square_size, speed, jump
def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)

def playsound(channel,audiofile):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(audiofile))
disable_controls = False
playerx = 250
playery = 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption(GameName)
done = False
# pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()
velocityY = 0
while not done:
        clock.tick(fps)
        screen.fill(BLUE)
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)
        player_hitbox = pygame.draw.rect(screen, GRAY, [playerx - 1, playery - 1,square_size + 1,square_size + 1])
        background = pygame.draw.rect(screen, BLACK, [0,0,500,500])
        ground_square = pygame.draw.rect(screen, GREEN, [0,300,500,500])
        player_square = pygame.draw.rect(screen, player_color, [playerx,playery,square_size,square_size])

        # Player movement
        if pygame.Rect.colliderect(player_hitbox, ground_square) == 0:
            playery = playery + gravity
        if not velocityY == 0:
            playery = playery - velocityY
            velocityY = velocityY - 1

        # Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        state = pygame.key.get_pressed()
        if state[pygame.K_a]:
            if disable_controls == False:
                playerx = playerx - speed
        if state[pygame.K_d]:
            if disable_controls == False:
                playerx = playerx + speed
        if state[pygame.K_w]:
            if disable_controls == False:
                if pygame.Rect.colliderect(player_hitbox, ground_square) == 1:
                    playery = playery - jump
        if state[pygame.K_LEFT]:
            if disable_controls == False:
                playerx = playerx - speed
        if state[pygame.K_RIGHT]:
            if disable_controls == False:
                playerx = playerx + speed
        if state[pygame.K_UP]:
            if disable_controls == False:
                if pygame.Rect.colliderect(player_hitbox, ground_square) == 1:
                    velocityY = jump
        if state[pygame.K_ESCAPE]:
            done = True
            print("Quit")

        print(velocityY)
        print(playerx)
        print(playery)
        pygame.display.update()
        pygame.display.flip()
