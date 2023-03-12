import pygame
from pygame_gui.elements import UIButton

import settings

from pygame_gui import UIManager, UI_BUTTON_PRESSED
from pocket_monster_world.state import GameState


class MenuState(GameState):
    name = "menu"

    def __init__(self, game):
        super().__init__(game)
        self.gui = UIManager((settings.SCR_WIDTH, settings.SCR_HEIGHT))
        self.btn_new_game = UIButton(
            relative_rect=pygame.Rect((settings.SCR_WIDTH / 2) - 100, (settings.SCR_HEIGHT / 2) - 250, 200, 50),
            text="New Game",
            manager=self.gui)
        self.btn_load_game = UIButton(
            relative_rect=pygame.Rect((settings.SCR_WIDTH / 2) - 100, (settings.SCR_HEIGHT / 2) - 150, 200, 50),
            text="Load Game",
            manager=self.gui)
        self.btn_options = UIButton(
            relative_rect=pygame.Rect((settings.SCR_WIDTH / 2) - 100, (settings.SCR_HEIGHT / 2) - 50, 200, 50),
            text="Options",
            manager=self.gui)
        self.btn_quit = UIButton(
            relative_rect=pygame.Rect((settings.SCR_WIDTH / 2) - 100, (settings.SCR_HEIGHT / 2) + 50, 200, 50),
            text="Quit",
            manager=self.gui)

    def handle_input(self):
        for event in self.game.events:
            self.gui.process_events(event)
            if event.type == UI_BUTTON_PRESSED:
                if event.ui_element == self.btn_new_game:
                    print("New Game")
                elif event.ui_element == self.btn_load_game:
                    print("Load Game")
                elif event.ui_element == self.btn_options:
                    print("Options")
                elif event.ui_element == self.btn_quit:
                    pygame.quit()
                    quit()

    def update(self):
        self.gui.update(self.game.dt)

    def shadow_update(self):
        pass

    def render(self):
        self.gui.draw_ui(self.game.screen)

    def shadow_render(self):
        pass

    def on_enter(self):
        pygame.mixer.music.load("assets/midi/mus_rg_gym.mid")
        pygame.mixer.music.play(-1, 0.0, 5000)

    def on_exit(self):
        pygame.mixer.music.fadeout(1000)
