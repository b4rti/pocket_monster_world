import pygame
import sys

from pygame import Rect

from pocket_monster_world.game_state import GameState
from pocket_monster_world.gui import UIPanel
from pocket_monster_world.gui.button import UIButton


class MainMenuPanel(UIPanel):

    def __init__(self, game):
        new_game_btn = UIButton(game, True,
                                Rect(game.screen.get_width() / 2 - 100, 100, 200, 40),
                                {"click": lambda: print("New Game")}, "New Game")

        load_game_btn = UIButton(game, True,
                                 Rect(game.screen.get_width() / 2 - 100, 150, 200, 40),
                                 {"click": lambda: print("Load Game")}, "Load Game")

        options_btn = UIButton(game, True,
                               Rect(game.screen.get_width() / 2 - 100, 200, 200, 40),
                               {"click": lambda: print("Options")}, "Options")

        quit_btn = UIButton(game, True,
                            Rect(game.screen.get_width() / 2 - 100, 250, 200, 40),
                            {"click": lambda: sys.exit()}, "Quit")

        super().__init__(game, True, Rect(0, 0, game.cfg.SCR_WIDTH, game.cfg.SCR_HEIGHT),
                         [new_game_btn, load_game_btn, options_btn, quit_btn])


class NewGamePanel(UIPanel):

    def __init__(self, game):
        super().__init__(game, True, Rect(0, 0, game.cfg.SCR_WIDTH, game.cfg.SCR_HEIGHT), [])


class LoadGamePanel(UIPanel):

    def __init__(self, game):
        super().__init__(game, True, Rect(0, 0, game.cfg.SCR_WIDTH, game.cfg.SCR_HEIGHT), [])


class OptionsPanel(UIPanel):

    def __init__(self, game):
        super().__init__(game, True, Rect(0, 0, game.cfg.SCR_WIDTH, game.cfg.SCR_HEIGHT), [])


class MenuState(GameState):
    name = "menu"

    def __init__(self, game):
        super().__init__(game)
        self.main_menu_panel = MainMenuPanel(game)
        self.new_game_panel = NewGamePanel(game)

    def handle_input(self):
        self.main_menu_panel.handle_input()

    def update(self):
        self.main_menu_panel.update()

    def shadow_update(self):
        pass

    def render(self):
        self.game.screen.fill((255, 255, 255))
        self.main_menu_panel.render()

    def shadow_render(self):
        pass

    def on_enter(self):
        pygame.mixer.music.load("assets/midi/mus_rg_gym.mid")
        pygame.mixer.music.play(-1, 0.0, 2500)

    def on_exit(self):
        pygame.mixer.music.fadeout(1000)
