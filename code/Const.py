# C
import pygame
from pygame.examples.grid import WINDOW_WIDTH, WINDOW_HEIGHT

C_BLACK = (0, 0, 0)
C_BLUE = (76, 121, 146)
C_CYAN = (0, 128, 128)
C_GREEN = (0, 126, 0)
C_ORANGE = (255, 165, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)

# E
ENTITY_DAMAGE = {'Level1BG0': 0,
                 'Level1BG1': 0,
                 'Level1BG2': 0,
                 'Level1BG3': 0,
                 'Level1BG4': 0,
                 'Level1BG5': 0,
                 'Level2BG0': 0,
                 'Level2BG1': 0,
                 'Level2BG2': 0,
                 'Level2BG3': 0,
                 'Level2BG4': 0,
                 'Player1': 1,
                 'Player1Shot': 25,
                 'Player2': 1,
                 'Player2Shot': 20,
                 'Enemy1': 1,
                 'Enemy1Shot': 20,
                 'Enemy2': 1,
                 'Enemy2Shot': 15,
                 }

ENTITY_HEALTH = {'Level1BG0': 999,
                 'Level1BG1': 999,
                 'Level1BG2': 999,
                 'Level1BG3': 999,
                 'Level1BG4': 999,
                 'Level1BG5': 999,
                 'Level2BG0': 999,
                 'Level2BG1': 999,
                 'Level2BG2': 999,
                 'Level2BG3': 999,
                 'Level2BG4': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 50,
                 'Enemy1Shot': 1,
                 'Enemy2': 60,
                 'Enemy2Shot': 1,
                 }

ENTITY_SCORE = {'Level1BG0': 0,
                'Level1BG1': 0,
                'Level1BG2': 0,
                'Level1BG3': 0,
                'Level1BG4': 0,
                'Level1BG5': 0,
                'Level2BG0': 0,
                'Level2BG1': 0,
                'Level2BG2': 0,
                'Level2BG3': 0,
                'Level2BG4': 0,
                'Player1': 0,
                'Player1Shot': 0,
                'Player2': 0,
                'Player2Shot': 0,
                'Enemy1': 100,
                'Enemy1Shot': 0,
                'Enemy2': 125,
                'Enemy2Shot': 0,
                }

ENTITY_SHOT_DELAY = {'Player1': 40,
                     'Player2': 20,
                     'Enemy1': 50,
                     'Enemy2': 200
                     }

ENTITY_SPEED = {'Level1BG0': 0,
                'Level1BG1': 2,
                'Level1BG2': 3,
                'Level1BG3': 4,
                'Level1BG4': 2,
                'Level1BG5': 3,
                'Level2BG0': 0,
                'Level2BG1': 2,
                'Level2BG2': 3,
                'Level2BG3': 4,
                'Level2BG4': 2,
                'Player1': 3,
                'Player1Shot': 7,
                'Player2': 3,
                'Player2Shot': 7,
                'Enemy1': 2,
                'Enemy1Shot': 5,
                'Enemy2': 1,
                'Enemy2Shot': 2,
                }

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = ('NEW GAME 1 PLAYER',
               'NEW GAME 2 PLAYERS - COOPERATIVE',
               'NEW GAME 2 PLAYERS - COMPETITIVE',
               'SCORE',
               'EXIT'
               )

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
SCORE_POS = {'Title': (WINDOW_HEIGHT / 2, 50),
             'EnterName': (WINDOW_WIDTH / 2, 80),
             'Label': (WINDOW_WIDTH / 2, 90),
             'Name': (WINDOW_WIDTH / 2, 110),
             0: (WINDOW_WIDTH / 2, 110),
             1: (WINDOW_WIDTH / 2, 130),
             2: (WINDOW_WIDTH / 2, 150),
             3: (WINDOW_WIDTH / 2, 170),
             4: (WINDOW_WIDTH / 2, 190),
             5: (WINDOW_WIDTH / 2, 210),
             6: (WINDOW_WIDTH / 2, 230),
             7: (WINDOW_WIDTH / 2, 250),
             8: (WINDOW_WIDTH / 2, 270),
             9: (WINDOW_WIDTH / 2, 290),
             }

SPAWN_TIME = 2500

# T
TIMEOUT_LEVEL = 20000
TIMEOUT_STEP = 100

# W
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324