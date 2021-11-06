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
from shared import size, GameName, fps, background_color, BLACK, RED, GREEN, BLUE, WHITE, GRAY, player_color, square_size, speed, jump
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

while not done:
        clock.tick(fps)
        screen.fill(BLUE)
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)
        player_hitbox = pygame.draw.rect(screen, GRAY, [playerx - 1, playery - 1,square_size + 1,square_size + 1])
        background = pygame.draw.rect(screen, BLACK, [0,0,500,500])
        ground_square = pygame.draw.rect(screen, GREEN, [0,300,500,500])
        player_square = pygame.draw.rect(screen, player_color, [playerx,playery,square_size,square_size])
        if pygame.Rect.colliderect(player_hitbox, ground_square) == 0:
            playery = playery + 1

        # Controls
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if disable_controls == False:
                        playerx = playerx - speed
                if event.key == pygame.K_d:
                    if disable_controls == False:
                        playerx = playerx + speed
                if event.key == pygame.K_w:
                    if disable_controls == False:
                        playery = playery - jump
                if event.key == pygame.K_s:
                    if disable_controls == False:
                        playery = playery + speed
                if event.key == pygame.K_LEFT:
                    if disable_controls == False:
                        playerx = playerx - speed
                if event.key == pygame.K_RIGHT:
                    if disable_controls == False:
                        playerx = playerx + speed
                if event.key == pygame.K_UP:
                    if disable_controls == False:
                        playery = playery - jump
                if event.key == pygame.K_DOWN:
                    if disable_controls == False:
                        playery =playery + speed
                if event.key == pygame.K_ESCAPE:
                    done = True
                    if show_debug == True:
                        print("Quit")
        print(playerx)
        print(playery)
        pygame.display.update()
        pygame.display.flip()
