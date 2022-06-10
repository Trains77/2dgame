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
from shared import size, show_debug, enable_program, system_recommends, PlayerName, GameName, gravity, fps, background_color, BLACK, RED, GREEN, BLUE, WHITE, GRAY, player_color, square_size, speed, jump
def image_display(surface, filename, xy):
    img = pygame.image.load(filename)
    surface.blit(img, xy)

if not platform.system() == system_recommends:
    print(style.BOLD + fore.RED + "Warning: Your " + platform.system() + " system may not work with this program" + style.RESET)


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
enemy1_on_ground = False
player_on_ground = False
player_on_roof = False
enemy1_on_roof = False
camera = [0, 0]
# pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()
velocityY = 0
def enemy_movement(enemy_pos, EnemyVelocity, enemyid, enemyAlive, enemy_on_ground, Enemy_On_Roof):
    finished = done
    enemyid = pygame.draw.rect(screen, BLACK, [enemy_pos[0] - 1, enemy1_pos[1] - 1, square_size + 1 ,square_size + 1])
    if enemyAlive == True:
        enemyid = pygame.draw.rect(screen, RED, [enemy_pos[0],enemy_pos[1],square_size,square_size])
    if enemy_pos[0] > playerx:
        enemy_pos[0] = enemy_pos[0] - speed / 2
    if enemy_pos[0] < playerx:
        enemy_pos[0] = enemy_pos[0] + speed / 2
    if enemy_pos[1] > playery:
        if enemy_pos[0] == playerx:
            if enemy_on_ground == True:
                if Enemy_On_Roof == False:
                    EnemyVelocity = jump * 0.8
    if enemy_on_ground == False:
        enemy_pos[1] = enemy_pos[1] + gravity
    if Enemy_On_Roof == True:
        EnemyVelocity = 0
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

def create_ground(COLOR, x, y, length, width):
    players_on_ground = player_on_ground
    enemy1s_on_ground = enemy1_on_ground
    players_on_roof = player_on_roof
    enemy1s_on_roof = enemy1_on_roof
    ground_square = pygame.draw.rect(screen, COLOR, [x,y,length,width])
    if pygame.Rect.colliderect(player_hitbox, ground_square) == 1:
        players_on_ground = True
    if pygame.Rect.colliderect(ground_square, enemy1_hitbox) == 1:
        enemy1s_on_ground = True
    if pygame.Rect.colliderect(player_top, ground_square) == 1:
        players_on_roof = True
    if pygame.Rect.colliderect(enemy1_top, ground_square) == 1:
        enemy1s_on_roof = True
    return players_on_ground, enemy1s_on_ground, players_on_roof, enemy1s_on_roof
while not done:
        clock.tick(fps)
        screen.fill(BLUE)
        mouse_button_list = pygame.mouse.get_pressed(num_buttons=3)
        player_hitbox = pygame.draw.rect(screen, GRAY, [playerx - 1, playery - 1,square_size + 1,square_size + 1])
        enemy1_hitbox = pygame.draw.rect(screen, WHITE, [enemy1_pos[0], enemy1_pos[1],square_size,square_size])
        enemy1_top = pygame.draw.rect(screen, RED, [enemy1_pos[0], enemy1_pos[1],square_size, square_size / 4])
        player_top = pygame.draw.rect(screen, BLUE, [playerx, playery - 1,square_size + 1,square_size / 4])
        background = pygame.draw.rect(screen, BLACK, [0,0,500,500])
        player_on_ground, enemy1_on_ground, player_on_roof, enemy1_on_roof = create_ground(GREEN, 50, 450, 400, 10)
        player_on_ground, enemy1_on_ground, player_on_roof, enemy1_on_roof = create_ground(GREEN, 200, 200, 100, 10)
        player_on_ground, enemy1_on_ground, player_on_roof, enemy1_on_roof = create_ground(GREEN, 150, 375, 50, 10)
        player_on_ground, enemy1_on_ground, player_on_roof, enemy1_on_roof = create_ground(GREEN, 225, 300, 50, 10)

        player_square = pygame.draw.rect(screen, player_color, [playerx,playery,square_size,square_size])

        # Player movement
        if player_on_ground == False:
           playery = playery + gravity
        if not velocityY == 0:
            if player_on_roof == False:
                playery = playery - velocityY
                velocityY = velocityY - 1
        if player_on_roof == True:
            velocityY = 0
            playery = playery + gravity


        enemy1_pos, EnemyVelocity1, enemy1Alive, done = enemy_movement(enemy1_pos, EnemyVelocity1, enemy1_hitbox, enemy1Alive, enemy1_on_ground, enemy1_on_roof)
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
                if player_on_ground == True:
                    if player_on_roof == False:
                        velocityY = jump
        if state[pygame.K_LEFT]:
            if disable_controls == False:
                playerx = playerx - speed
        if state[pygame.K_RIGHT]:
            if disable_controls == False:
                playerx = playerx + speed
        if state[pygame.K_UP]:
            if disable_controls == False:
                if player_on_ground == True:
                    if player_on_roof == False:
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
        # Reset entity falling variable
        player_on_ground = False
        enemy1_on_ground = False
        player_on_roof = False
        enemy1_on_roof = False
