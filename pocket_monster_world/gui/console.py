import pygame

from pocket_monster_world.gui import GuiElement


class Console(GuiElement):
    def __init__(self, game: 'Game'):
        super().__init__(game)
        self.font = pygame.font.Font("assets/font/pokemon.ttf", 30)
        self.text = ""
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.topleft = (0, 0)
        self.text_rect.width = 800
        self.text_rect.height = 600