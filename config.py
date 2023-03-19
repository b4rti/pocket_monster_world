import pygame as pg


# ======== #
# Display  #
# ======== #

SCR_WIDTH       = 3440 # 960
SCR_HEIGHT      = 1440 # 540
SCR_FLAGS       = pg.SCALED  # | pg.NOFRAME | pg.FULLSCREEN
SCR_DEPTH       = 32
SCR_FPS         = -1


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

SND_MAIN_VOL    = 0.1
SND_FX_VOL      = 1.0
SND_MUSIC_VOL   = 0.5
