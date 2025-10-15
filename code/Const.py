# C
import pygame

COLOR_BLACK = 0, 0, 0
COLOR_BLUE = 76, 121, 146
COLOR_ORANGE = 255, 165, 0
COLOR_WHITE = 255, 255, 255
COLOR_YELLOW = 255, 255, 0

# E
ENTITY_HEALTH = {'Level1BG0': 999,
                 'Level1BG1': 999,
                 'Level1BG2': 999,
                 'Level1BG3': 999,
                 'Level1BG4': 999,
                 'Level1BG5': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 50,
                 'Enemy1Shot': 1,
                 'Enemy2': 60,
                 'Enemy2Shot': 1,}

ENTITY_SHOT_DELAY = {'Player1': 40,
                     'Player2': 20,
                     'Enemy1': 50,
                     'Enemy2': 200}

ENTITY_SPEED = {'Level1BG0': 0,
                'Level1BG1': 2,
                'Level1BG2': 3,
                'Level1BG3': 4,
                'Level1BG4': 2,
                'Level1BG5': 3,
                'Player1': 3,
                'Player1Shot': 7,
                'Player2': 3,
                'Player2Shot': 7,
                'Enemy1': 2,
                'Enemy1Shot': 5,
                'Enemy2': 1,
                'Enemy2Shot': 2,}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME 1 PLAYER',
               'NEW GAME 2 PLAYERS - COOPERATIVE',
               'NEW GAME 2 PLAYERS - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_w,
                 'Player2': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                 'Player2': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                 'Player2': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                 'Player2': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL,
                    'Player2': pygame.K_RCTRL}

# S
SPAWN_TIME = 3000
# W
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324
