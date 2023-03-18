from pygame import Surface, Rect

from pocket_monster_world.gui import UIElement


class UIButton(UIElement):

    def __init__(self, game, visible: bool, rect: Rect, actions: dict[str, callable], text: str):
        super().__init__(game, visible, rect, actions)
        self.text = text

    def update(self):
        pass

    def render(self, target: Surface):
        target.fill((255, 255, 255), self.rect)
        text_pos = (self.rect.x + self.rect.width / 2 - self.game.font.size(self.text)[0] / 2,
                    self.rect.y + self.rect.height / 2 - self.game.font.size(self.text)[1] / 2)
        text_rect = Rect(text_pos[0], text_pos[1], self.game.font.size(self.text)[0], self.game.font.size(self.text)[1])
        target.blit(self.game.font.render(self.text, True, (0, 0, 0)), text_rect)
