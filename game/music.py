from time import sleep
import os
from shared import song, show_debug, enable_music
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import pydub
from pygame.locals import *
if enable_music == True:
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
    if show_debug == True:
        print("Playing Music")
elif enable_music == False:
    if show_debug == True:
        print("Music playing is disabled")

# Background music is owned by FesliyanStudios.
