# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 1.5,
    'Level1Bg3': 2,
    'Level1Bg4': 2.3,
    'Level1Bg5': 2,
    'Player 1': 3,
    'Player 1Shot': 5,
    'Player 2': 3,
    'Player 2Shot': 3,
    'Enemy1': 2,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Jogador 1Shot': 1,
    'Player2': 300,
    'Jogador 2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Jogador 1': 20,
    'Jogador 2': 15,
    'Enemy1': 80,
    'Enemy2': 170,
}

# M
MENU_OPTION = ('NEW GAME 1 PLAYER',
               'NEW GAME 2 PLAYERS - COOP',
               'NEW GAME 2 PLAYERS - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_w ,
                 'Player2': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                   'Player2': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                   'Player2': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                    'Player2': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL,
                    'Player2': pygame.K_SPACE}


# S
SPAWN_TIME = 40000

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324