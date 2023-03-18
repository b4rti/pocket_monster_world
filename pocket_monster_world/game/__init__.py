import pygame
import config
import sys

from enum import IntEnum

from pocket_monster_world.game.plugin import PluginManager
from pocket_monster_world.game_state import GameStateManager


class MouseButtons(IntEnum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3


class Game:
    def __init__(self):
        self.cfg = config
        
        pygame.init()
        pygame.display.set_caption('Pocket Monster World')

        pygame.mixer.init()
        pygame.mixer.set_num_channels(32)
        for i in range(32):
            pygame.mixer.Channel(i).set_volume(self.cfg.SND_FX_VOL*self.cfg.SND_MAIN_VOL)
        pygame.mixer.music.set_volume(self.cfg.SND_MUSIC_VOL*self.cfg.SND_MAIN_VOL)

        self.font = pygame.font.Font("assets/font/pokemon.ttf", 32)

        self.plugins = PluginManager(self)
        self.plugins.load_all()
        self.states = GameStateManager(self)

        self.screen = pygame.display.set_mode((self.cfg.SCR_WIDTH, self.cfg.SCR_HEIGHT))
        self.clock = pygame.time.Clock()
        self.fps: float = self.cfg.SCR_FPS
        self.dt: float = 0.0

        self.events: list[pygame.event.Event] = []
        self.keys_up: list[int] = []
        self.keys_down: list[int] = []
        self.mouse_btn_up: list[bool, bool, bool] = []
        self.mouse_btn_down: list[bool, bool, bool] = []
        self.mouse_wheel: int = 0
        self.mouse_pos: tuple[int, int] = (0, 0)
        self.mouse_rel: tuple[int, int] = (0, 0)

    def run(self):
        while True:
            self.dt = self.clock.tick(self.fps) / 1000.0
            self.handle_input()
            self.update()
            self.render()

    def handle_input(self):
        self.events = pygame.event.get()
        self.keys_up = []
        self.keys_down = []
        self.mouse_btn_up = []
        self.mouse_btn_down = []
        self.mouse_wheel = 0
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rel = pygame.mouse.get_rel()

        for event in self.events:
            if event.type == pygame.KEYUP:
                self.keys_up.append(event.key)
            elif event.type == pygame.KEYDOWN:
                self.keys_down.append(event.key)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_btn_up.append(event.button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_btn_down.append(event.button)
            elif event.type == pygame.MOUSEWHEEL:
                self.mouse_wheel = event.y
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if MouseButtons.LEFT.value in self.mouse_btn_up:
            self.mouse_btn_up[MouseButtons.LEFT.value - 1] = True

        self.plugins.handle_input()
        self.states.handle_input()

    def update(self):
        self.plugins.pre_update()
        self.states.update()
        self.plugins.post_update()

    def render(self):
        self.screen.fill((0, 0, 0))

        self.plugins.pre_render()
        self.states.render()
        self.plugins.post_render()

        pygame.display.update()
