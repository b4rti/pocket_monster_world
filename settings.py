import pygame as pg


# ======== #
# Display  #
# ======== #

SCR_WIDTH       = 800
SCR_HEIGHT      = 600
SCR_DEPTH       = 32
SCR_FLAGS       = pg.DOUBLEBUF | pg.HWSURFACE # | pg.NOFRAME
SCR_FPS         = 60


# ======== #
# Keyboard #
# ======== #

KB_UP           = [pg.K_w, pg.K_UP]
KB_DOWN         = [pg.K_s, pg.K_DOWN]
KB_LEFT         = [pg.K_a, pg.K_LEFT]
KB_RIGHT        = [pg.K_d, pg.K_RIGHT]

KB_ENTER        = [pg.K_RETURN, pg.K_KP_ENTER, pg.K_SPACE]
KB_BACK         = [pg.K_BACKSPACE, pg.K_ESCAPE]


# ======== #
#  Sound   #
# ======== #

SND_MAIN_VOL    = 0.33
SND_FX_VOL      = 1.0
SND_MUSIC_VOL   = 1.0
