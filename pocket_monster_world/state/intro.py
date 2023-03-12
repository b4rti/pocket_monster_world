import pygame

import settings
from pocket_monster_world.state import GameState
from pocket_monster_world.state.menu import MenuState


class IntroState(GameState):
    name = "intro"

    def __init__(self, game):
        super().__init__(game)
        self.logo = pygame.image.load("assets/img/logo.png")
        self.psyduck = pygame.image.load("assets/img/pokemon/psyduck/front_default.png")
        self.psyduck = pygame.transform.scale(self.psyduck, (300, 300))
        self.font = pygame.font.Font("assets/font/pokemon.ttf", 24)
        self.text = self.font.render("Press any key to continue...", True, (255, 255, 255))

    def handle_input(self):
        if any(key in self.game.keys_down for key in settings.KB_ENTER):
            self.game.states.change(MenuState(self.game))

    def update(self):
        pass

    def shadow_update(self):
        pass

    def render(self):
        self.game.screen.blit(self.logo, (75, 75))
        self.game.screen.blit(self.psyduck, (250, 150))

        if int(pygame.time.get_ticks() / 750) % 2 == 0:
            self.game.screen.blit(self.text, (300, 400))

    def shadow_render(self):
        pass

    def on_enter(self):
        path = "assets/midi/mus_rg_title.mid"
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1, 0.0, 5000)

    def on_exit(self):
        pygame.mixer.music.fadeout(1000)
