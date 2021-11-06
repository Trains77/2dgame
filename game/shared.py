# Stuff for variables
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

# Game Settings
GameName = "2D Python Game" # The name of the game
enable_music = True # Whether or not music is enabled
enable_audio = True # Whether or not audio should be played
Inv_Slot = 0 # Default inventory slot
enable_program = True # Enables or Disables the program
facing = "Right" # Default player rotation

# Color rgb codes
BLACK = (0, 0, 0) # The RGB code for Black
RED = (255, 0, 0) # The RGB code for Red
GREEN = (0, 255, 0) # The RGB code for Green
BLUE = (0, 0, 255) # The RGB code for Blue
GRAY = (200, 200, 200) # The RGB code for Gray
WHITE = (255, 255, 255) # The RGB code fro White

# Debugging settings
disable_background = False # Wether the game should load the background image
player_color = (255, 255, 255) # The color of the player's hitbox
block_color = GREEN # Default square color
dialog_color = (255, 255, 255) # Dialog box color
background_color = (128, 0, 128) # The background color of the game
show_debug = False # Enable debugging messages
enable_crash_debug = False # Enables keybind to cause a game crash

# File paths
item_path = "Textures/items/" # Where to pull item textures from
environment_audio_path = "Audio/Environment/" # Where to pull environment audio from
environment_path = "Textures/Environment/" # Where to pull environmental textures from
characters_path = "Textures/Characters/" # Where to pull character textures from
transparent_prefix = "transparent_" # The prefix to use when retrieving transparent files
flipped_prefix = "flipped_" # The prefix for getting flipped item textures

# Internal variables, changing them will cause issues
size = [500, 500] # The size of the screen
square_size = 20 # How big the default hitbox is
# item_size = 10 # The size of an item's hitbox
fps = 60 # The FPS of the game
inv = [0, 0, 0, 0, 0, 0] # Inventory list
minimum_slot = 80 # The default coordinates of slot 0
# gameIcon = pygame.image.load('Textures/Icons/game.png') # Path to game's window icon
mapid = 0 # Starting map id, currently unused
system_recommends = "Linux" # The system(s) that the script is verified to work with
version = "0.01"
speed = 10
jump = 50
