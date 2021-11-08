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
from shared import size, show_debug, PlayerName, GameName, gravity, fps, background_color, BLACK, RED, GREEN, BLUE, WHITE, GRAY, player_color, square_size, speed, jump
def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)

def playsound(channel,audiofile):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(audiofile))
def killplayer(DeathMessage):
    if DeathMessage == "OUT_OF_WORLD":
        print(fore.RED + PlayerName + " fell out of the world" + style.RESET)
    elif DeathMessage == "NERD":
        print(fore.RED + PlayerName + " was a nerd." + style.RESET)
    elif DeathMessage == "ENEMY_KILL":
        print(fore.RED + PlayerName + " was killed by an enemy" + style.RESET)
    else:
        print(PlayerName + " died")
    done = True
    return done
disable_controls = False
playerx = 250
playery = 0
enemy1_pos = [100, 0]
enemy1Alive = True
EnemyVelocity1 = 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption(GameName)
done = False
# pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()
velocityY = 0
def enemy_movement(enemy_pos, EnemyVelocity, enemyid, enemyAlive):
    finished = done
    enemyid = pygame.draw.rect(screen, BLACK, [enemy_pos[0] - 1, enemy1_pos[1] - 1,square_size + 1,square_size + 1])
    if enemyAlive == True:
        enemy1_square = pygame.draw.rect(screen, RED, [enemy1_pos[0],enemy1_pos[1],square_size,square_size])
    if enemy_pos[0] > playerx:
        enemy_pos[0] = enemy_pos[0] - speed / 2
    if enemy_pos[0] < playerx:
        enemy_pos[0] = enemy_pos[0] + speed / 2
    if enemy_pos[1] > playery:
        if enemy_pos[0] == playerx:
            if pygame.Rect.colliderect(enemyid, ground_square) == 1:
                EnemyVelocity = jump * 0.7
    if pygame.Rect.colliderect(enemyid, ground_square) == 0:
        enemy_pos[1] = enemy_pos[1] + gravity
    if not EnemyVelocity <= 0:
        enemy_pos[1] = enemy_pos[1] - EnemyVelocity
        EnemyVelocity = EnemyVelocity - 1
    #
    if pygame.Rect.colliderect(player_hitbox, enemyid) == 1:
        finished = killplayer("ENEMY_KILL")
    if enemy_pos[1] > 500:
        enemyAlive = False
    return enemy_pos, EnemyVelocity, enemyAlive, finished
while not done:
        clock.tick(fps)
        screen.fill(BLUE)
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)
        player_hitbox = pygame.draw.rect(screen, GRAY, [playerx - 1, playery - 1,square_size + 1,square_size + 1])
        enemy1_hitbox = pygame.draw.rect(screen, WHITE, [enemy1_pos[0] - 1, enemy1_pos[1] - 1,square_size + 1,square_size + 1])
        background = pygame.draw.rect(screen, BLACK, [0,0,500,500])
        ground_square = pygame.draw.rect(screen, GREEN, [0,300,500,500])
        player_square = pygame.draw.rect(screen, player_color, [playerx,playery,square_size,square_size])
        # Player movement
        if pygame.Rect.colliderect(player_hitbox, ground_square) == 0:
            playery = playery + gravity
        if not velocityY == 0:
            playery = playery - velocityY
            velocityY = velocityY - 1

        enemy1_pos, EnemyVelocity1, enemy1Alive, done = enemy_movement(enemy1_pos, EnemyVelocity1, enemy1_hitbox, enemy1Alive)
        # Enemy movement

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
                    velocityY = jump
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

        if playery > 500:
            done = killplayer("OUT_OF_WORLD")
        if show_debug == True:
            print("Player Velocity: " + str(velocityY))
            print("Player Cords: " + str(playerx) + ", " + str(playery))
        pygame.display.update()
        pygame.display.flip()
