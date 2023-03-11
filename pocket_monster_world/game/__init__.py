import pygame
import settings
import sys

from pocket_monster_world.game.plugin import PluginManager
from pocket_monster_world.gui import GuiManager
from pocket_monster_world.state import GameStateManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pocket Monster World')
        pygame.mixer.init()
        pygame.mixer.set_num_channels(32)
        for i in range(32):
            pygame.mixer.Channel(i).set_volume(settings.SND_FX_VOL*settings.SND_MAIN_VOL)
        pygame.mixer.music.set_volume(settings.SND_MUSIC_VOL*settings.SND_MAIN_VOL)

        self.plugins = PluginManager(self)
        self.plugins.load_all()
        self.states = GameStateManager(self)
        self.gui = GuiManager(self)

        self.screen = pygame.display.set_mode(
            (settings.SCR_WIDTH, settings.SCR_HEIGHT),
            settings.SCR_FLAGS,
            settings.SCR_DEPTH)
        self.clock = pygame.time.Clock()
        self.fps: float = settings.SCR_FPS
        self.dt: float = 0.0

        self.events: list[pygame.event.Event] = []
        self.keys: dict[int, bool] = {}
        self.keys_down: list[int] = []
        self.keys_up: list[int] = []
        self.mouse_btn: tuple[bool, bool, bool] = (False, False, False)
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
        self.keys_down = []
        self.keys_up = []
        self.keys = pygame.key.get_pressed()
        self.mouse_btn = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rel = pygame.mouse.get_rel()

        for event in self.events:
            if event.type == pygame.KEYDOWN:
                self.keys_down.append(event.key)
            elif event.type == pygame.KEYUP:
                self.keys_up.append(event.key)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.plugins.handle_input()
        self.states.handle_input()
        self.gui.handle_input()

    def update(self):
        self.plugins.pre_update()
        self.states.update()
        self.gui.update()
        self.plugins.post_update()

    def render(self):
        self.screen.fill((0, 0, 0))

        self.plugins.pre_render()
        self.states.render()
        self.gui.render()
        self.plugins.post_render()

        pygame.display.update()
