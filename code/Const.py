# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_BLUE = (0, 0, 255)

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
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 1.5,
    'Level2Bg3': 2,
    'Level2Bg4': 2.3,
    'Jogador 1': 3,
    'Jogador 1Shot': 5,
    'Jogador 2': 3,
    'Jogador 2Shot': 3,
    'Enemy1': 2,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 3.5
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Jogador 1': 0,
    'Jogador 1Shot': 0,
    'Jogador 2': 0,
    'Jogador 2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Jogador 1': 300,
    'Jogador 1Shot': 1,
    'Jogador 2': 300,
    'Jogador 2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Jogador 1': 1,
    'Jogador 1Shot': 25,
    'Jogador 2': 1,
    'Jogador 2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SHOT_DELAY = {
    'Jogador 1': 20,
    'Jogador 2': 15,
    'Enemy1': 30,
    'Enemy2': 45
}

# M
MENU_OPTION = ('NEW GAME 1 PLAYER',
               'NEW GAME 2 PLAYERS - COOP',
               'NEW GAME 2 PLAYERS - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Jogador 1': pygame.K_w ,
                 'Jogador 2': pygame.K_UP}
PLAYER_KEY_DOWN = {'Jogador 1': pygame.K_s,
                   'Jogador 2': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Jogador 1': pygame.K_a,
                   'Jogador 2': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Jogador 1': pygame.K_d,
                    'Jogador 2': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Jogador 1': pygame.K_LCTRL,
                    'Jogador 2': pygame.K_RCTRL}


# S
SPAWN_TIME = 2700

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }