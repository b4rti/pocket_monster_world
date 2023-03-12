import os

import pygame
import settings

from pocket_monster_world.state import GameState


class MenuState(GameState):
    name = "menu"

    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font("assets/font/pokemon.ttf", 30)

    def handle_input(self):
        if any(key in self.game.keys_down for key in settings.KB_BACK):
            pygame.quit()
            exit()

    def update(self):
        pass

    def shadow_update(self):
        pass

    def render(self):
        pass

    def shadow_render(self):
        pass

    def on_enter(self):
        path = "assets/midi/mus_rg_gym.mid"
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1, 0.0, 5000)

    def on_exit(self):
        pygame.mixer.music.fadeout(1000)
