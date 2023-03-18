import pygame
from pygame import Rect

from pocket_monster_world.game_state import GameState
from pocket_monster_world.gui import UIPanel
from pocket_monster_world.gui.button import UIButton


class MainMenuPanel(UIPanel):

    def __init__(self, game):
        # conter position of the button
        button_pos = (game.screen.get_width() / 2 - 50, game.screen.get_height() / 2 - 25)
        button = UIButton(game, True, Rect(button_pos[0], button_pos[1], 100, 50), {"click": self.on_click}, "Click Me")
        super().__init__(game, True, Rect(0, 0, 800, 600), [button])

    def on_click(self):
        print("Clicked!")


class MenuState(GameState):
    name = "menu"

    def __init__(self, game):
        super().__init__(game)
        self.panel = MainMenuPanel(game)

    def handle_input(self):
        self.panel.handle_input()

    def update(self):
        self.panel.update()

    def shadow_update(self):
        pass

    def render(self):
        self.panel.render()

    def shadow_render(self):
        pass

    def on_enter(self):
        pygame.mixer.music.load("assets/midi/mus_rg_gym.mid")
        pygame.mixer.music.play(-1, 0.0, 5000)

    def on_exit(self):
        pygame.mixer.music.fadeout(1000)
