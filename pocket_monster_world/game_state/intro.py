import pygame

from pocket_monster_world.game_state import GameState
from pocket_monster_world.game_state.menu import MenuState


class IntroState(GameState):
    name = "intro"

    def __init__(self, game):
        super().__init__(game)
        self.logo = pygame.image.load("assets/img/logo.png")
        self.logo = pygame.transform.scale(self.logo, (700, 200))
        self.psyduck = pygame.image.load("assets/img/pokemon/psyduck/front_default.png")
        self.psyduck = pygame.transform.scale(self.psyduck, (400, 400))
        self.font = pygame.font.Font("assets/font/pokemon.ttf", 32)
        self.text = self.font.render("Press any key to continue...", False, (255, 255, 255))

    def handle_input(self):
        if len(self.game.keys_down) or any(self.game.mouse_btn):
            self.game.states.change(MenuState(self.game))

    def update(self):
        pass

    def shadow_update(self):
        pass

    def render(self):
        self.game.screen.blit(self.logo, (50, 25))
        self.game.screen.blit(self.psyduck, (200, 100))

        if int(pygame.time.get_ticks() / 750) % 2 == 0:
            self.game.screen.blit(self.text, (265, 450))

    def shadow_render(self):
        pass

    def on_enter(self):
        pygame.mixer.music.load("assets/midi/mus_rg_title.mid")
        pygame.mixer.music.play(-1, 0.0, 5000)

    def on_exit(self):
        pygame.mixer.music.fadeout(1000)
