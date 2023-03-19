import pygame
from pygame import Font, Surface

from pocket_monster_world.game_state import GameState
from pocket_monster_world.game_state.menu import MenuState


class IntroState(GameState):
    name = "intro"

    def __init__(self, game):
        super().__init__(game)
        self.font: Font = pygame.font.Font("assets/font/pokemon.ttf", 24)
        self.logo: Surface = pygame.image.load("assets/img/logo.png").convert_alpha()
        self.logo: Surface = pygame.transform.scale(self.logo, (400, 100))
        self.psyduck: Surface = pygame.image.load("assets/img/pokemon/psyduck/front_default.png").convert_alpha()
        self.psyduck: Surface = pygame.transform.scale(self.psyduck, (350, 350))
        self.text: Surface = self.font.render("Press any key to continue...", False, (0, 0, 0))

    def handle_input(self):
        if len(self.game.keys_down) or any(self.game.mouse_btn_up):
            self.game.states.change(MenuState(self.game))

    def update(self):
        pass

    def shadow_update(self):
        pass

    def render(self):
        self.game.screen.fill((255, 255, 255))
        logo_pos = (self.game.cfg.SCR_WIDTH / 2 - self.logo.get_width() / 2, self.game.cfg.SCR_HEIGHT / 10)
        self.game.screen.blit(self.logo, logo_pos)
        psyduck_pos = (self.game.cfg.SCR_WIDTH / 2 - self.psyduck.get_width() / 2, self.game.cfg.SCR_HEIGHT / 5)
        self.game.screen.blit(self.psyduck, psyduck_pos)

        text_pos = (self.game.cfg.SCR_WIDTH / 2 - self.text.get_width() / 2, self.game.cfg.SCR_HEIGHT / 4 * 3)
        if int(pygame.time.get_ticks() / 750) % 2 == 0:
            self.game.screen.blit(self.text, text_pos)

    def shadow_render(self):
        pass

    def on_enter(self):
        pygame.mixer.music.load("assets/midi/mus_rg_title.mid")
        pygame.mixer.music.play(-1, 0.0, 2500)

    def on_exit(self):
        pygame.mixer.music.fadeout(1000)
