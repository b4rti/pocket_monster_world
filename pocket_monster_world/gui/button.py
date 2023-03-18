import pygame.draw
from pygame import Surface, Rect

from pocket_monster_world.gui import UIElement


class UIButton(UIElement):

    def __init__(self, game, visible: bool, rect: Rect, actions: dict[str, callable], text: str):
        actions["hover"] = self._hover
        actions["unhover"] = self._unhover

        super().__init__(game, visible, rect, actions)

        self.text = text
        self.bg_color = (255, 255, 255)
        self.fg_color = (0, 0, 0)

    def update(self):
        pass

    def render(self, target: Surface):
        target.fill(self.bg_color, self.rect)
        text_pos = (self.rect.x + self.rect.width / 2 - self.game.font.size(self.text)[0] / 2,
                    self.rect.y + self.rect.height / 2 - self.game.font.size(self.text)[1] / 2)
        text_rect = Rect(text_pos[0], text_pos[1], self.game.font.size(self.text)[0], self.game.font.size(self.text)[1])
        target.blit(self.game.font.render(self.text, False, self.fg_color), text_rect)
        pygame.draw.rect(target, self.fg_color, self.rect, 1)

    def _hover(self):
        self.bg_color = (200, 200, 200)

    def _unhover(self):
        self.bg_color = (255, 255, 255)
