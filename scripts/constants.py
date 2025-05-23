import pygame

pygame.init()
info = pygame.display.Info()

screen_width, screen_height = info.current_w, info.current_h
DISPLAY_SIZE = (screen_width, screen_height)
aspect_x = DISPLAY_SIZE[0] - (DISPLAY_SIZE[0] % 16)
aspect_y = DISPLAY_SIZE[1] - (DISPLAY_SIZE[1] % 9)
DISPLAY_SIZE = (aspect_x, aspect_y)

FPS = 60

TILE_SIZE = DISPLAY_SIZE[0] // 28 # tilemap tile size

PLAYER_SPEED = 0.8   *TILE_SIZE/36 # added per frame
JUMP_SPEED = 14  *TILE_SIZE/36 # initial jump velocity
WALLSLIDE_SPEED = 0.7  *TILE_SIZE/36 # the speed in which the player will slide off a wall
WALLJUMP_X_SPEED = 9  *TILE_SIZE/36 # the x velocity of the player when jumpingoff of a wall
WALLJUMP_Y_SPEED = 15  *TILE_SIZE/36 # the y velocity of the player when jumpingoff of a wall
GRAVITY_UP = 0.6   *TILE_SIZE/36 # subtracted from y velocity every frame when player going up
GRAVITY_DOWN = 0.3  *TILE_SIZE/36 # subtracted from y velocity every frame when player going down
ACCELERAION = 0.001  *TILE_SIZE/36 # friction with the ground on the x axis when starting to move, between 0 and 1 (0 < Acc < 1)
DECCELARATION = 0.1   *TILE_SIZE/36 # friction with the ground on the x axis when stopping to move, between 0 and 1 (0 < Acc < 1)
MAX_X_SPEED = 10   *TILE_SIZE/36 # x axis speed limit
MAX_Y_SPEED = 18   *TILE_SIZE/36 # y axis speed limit

WALL_MOMENTUM_PRESERVE = 0.15  # Percentage of upward velocity preserved when hitting wall
WALL_MOMENTUM_FRAMES = 3 # amount of frames activated

PLAYER_BUFFER = 5 # amount of frame buffer
COYOTE_TIME = 3  # Player can jump for 6 frames after leaving a platform


PLAYERS_SIZE = (TILE_SIZE*0.8, TILE_SIZE*0.8) # size of actual player hitbox
PLAYERS_IMAGE_SIZE = (PLAYERS_SIZE[0], PLAYERS_SIZE[1]) # size of the player image

PHYSICS_TILES = {'grass', 'stone', 'hardened_clay', 'ores', 'weather', 'nether', 'wood'}
AUTOTILE_TYPES = {'grass', 'stone', 'hardened_clay', 'ores', 'weather','nether', 'wood'}
INTERACTIVE_TILES = {'spikes', 'finish', 'saws', 'kill'}
SPIKE_SIZE = (0.6, 0.25)
SAW_SIZE = 0.8

FONT = r'data\fonts\Menu.ttf' 

EDITOR_SCROLL_SPEED = 10 # how fast you can move in the editor using WASD

MENUBG = r'data\images\menugbg.png'

MENUTXTCOLOR = (120, 83, 58)
WHITE = (255, 255, 255)

def calculate_ui_constants(display_size):
    ref_width, ref_height = 1920, 1080
    
    width_scale = display_size[0] / ref_width
    height_scale = display_size[1] / ref_height
    general_scale = min(width_scale, height_scale)  
    
    return {
        'BUTTON_HEIGHT': int(80 * height_scale),
        'BUTTON_MIN_WIDTH': int(200 * width_scale),
        'BUTTON_TEXT_PADDING': int(40 * general_scale),
        'BUTTON_SPACING': int(20 * general_scale),
        'BUTTON_COLOR': (30, 45, 90, 220),      # Deep navy with slight transparency
        'BUTTON_HOVER_COLOR': (15, 25, 50, 200), # Darker navy with more transparency
        'BUTTON_GLOW_COLOR': (80, 130, 220),      # Bright blue (no opacity - for glow effects)
        'GRID_COLUMNS': 5,  
        'MAPS_PER_PAGE': 20  
    }

