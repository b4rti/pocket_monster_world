import pygame.draw
from pygame import Surface, Rect, Font

from pocket_monster_world.gui import UIElement


class UIButton(UIElement):

    def __init__(self, game, visible: bool, rect: Rect, actions: dict[str, callable], text: str):
        actions["hover"] = self._hover
        actions["unhover"] = self._unhover

        super().__init__(game, visible, rect, actions)

        self.font: Font = pygame.font.Font("assets/font/pokemon.ttf", 32)
        self.text: str = text
        self.bg_color: tuple[int, int, int] = (255, 255, 255)
        self.fg_color: tuple[int, int, int] = (0, 0, 0)
        self.surface: Surface = Surface((self.rect.width, self.rect.height))

    def update(self):
        pass

    def render(self, target: Surface):
        self.surface.fill(self.bg_color)
        pygame.draw.rect(self.surface, self.fg_color, self.surface.get_rect(), 3, border_radius=5)
        text_pos = (self.surface.get_width() / 2 - self.font.size(self.text)[0] / 2,
                    self.surface.get_height() / 2 - self.font.size(self.text)[1] / 2)
        text_rect = Rect(text_pos[0], text_pos[1], self.font.size(self.text)[0], self.font.size(self.text)[1])
        self.surface.blit(self.font.render(self.text, False, self.fg_color), text_rect)
        target.blit(self.surface, self.rect)

    def _hover(self):
        self.bg_color = (200, 200, 200)

    def _unhover(self):
        self.bg_color = (255, 255, 255)
