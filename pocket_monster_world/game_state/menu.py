import pygame
import sys

from pygame import Rect

from pocket_monster_world.game_state import GameState
from pocket_monster_world.game_state.world import WorldState
from pocket_monster_world.gui import UIPanel
from pocket_monster_world.gui.button import UIButton


class MainMenuPanel(UIPanel):

    def __init__(self, game):
        new_game_btn = UIButton(game, True,
                                Rect(game.cfg.SCR_WIDTH / 2 - 50, 125, 100, 25),
                                {"click": lambda: self._switch_panel(NewGamePanel(game))}, "New Game")

        load_game_btn = UIButton(game, True,
                                 Rect(game.cfg.SCR_WIDTH / 2 - 50, 155, 100, 25),
                                 {"click": lambda: self._switch_panel(LoadGamePanel(game))}, "Load Game")

        options_btn = UIButton(game, True,
                               Rect(game.cfg.SCR_WIDTH / 2 - 50, 185, 100, 25),
                               {"click": lambda: self._switch_panel(OptionsPanel(game))}, "Options")

        quit_btn = UIButton(game, True,
                            Rect(game.cfg.SCR_WIDTH / 2 - 50, 215, 100, 25),
                            {"click": lambda: sys.exit()}, "Quit")

        super().__init__(game, True, Rect(0, 0, game.cfg.SCR_WIDTH, game.cfg.SCR_HEIGHT),
                         [new_game_btn, load_game_btn, options_btn, quit_btn])

    def _switch_panel(self, panel):
        self.game.states["menu"].panel = panel


class NewGamePanel(UIPanel):

    def __init__(self, game):
        start_btn = UIButton(game, True,
                             Rect(game.screen.get_width() / 2 - 50, 125, 100, 25),
                             {"click": lambda: self.game.states.push(WorldState(self.game))}, "Start")

        super().__init__(game, True, Rect(0, 0, game.cfg.SCR_WIDTH, game.cfg.SCR_HEIGHT), [start_btn])


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
        self.panel = MainMenuPanel(game)

    def handle_input(self):
        self.panel.handle_input()

    def update(self):
        self.panel.update()

    def shadow_update(self):
        pass

    def render(self):
        self.game.screen.fill((255, 255, 255))
        self.panel.render()

    def shadow_render(self):
        pass

    def on_enter(self):
        pygame.mixer.music.load("assets/midi/mus_rg_gym.mid")
        pygame.mixer.music.play(-1, 0.0, 2500)

    def on_exit(self):
        pygame.mixer.music.fadeout(1000)
