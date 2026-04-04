#C
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 1000,
    'Player1Shot': 1,
    'Enemy1': 200,
    'Enemy1Shot': 1,
    'Enemy2': 300,
    'Enemy2Shot': 1,

}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 0,
    'Player1Shot': 50,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 6,
    'Player1Shot': 7,
    'Enemy1': 2,
    'Enemy1Shot': 6,
    'Enemy2': 2,
    'Enemy2Shot': 7,
}

ENTITY_SHOT_DELAY = {
    'Player1': 15,
    'Enemy1': 70,
    'Enemy2': 70,
}

#M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player1': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_d}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE}


#S
SPAWN_TIME = 4000

#T
TIMEOUT_LEVEL = 30000 #20s
TIMEOUT_STEP = 100 #100ms

#W
WIN_WIDTH = 576
WIN_HEIGHT = 848
#img size

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
             9: (WIN_WIDTH / 2, 290)
             }