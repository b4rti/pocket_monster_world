from abc import ABCMeta, abstractmethod
from pygame import Surface, Rect
from pocket_monster_world.game.enums import MouseButtons


class UIElement(metaclass=ABCMeta):

    def __init__(self, game, visible: bool, rect: Rect, actions: dict[str, callable]):
        self.game = game
        self.visible = visible
        self.rect: Rect = rect
        self.actions: dict[str, callable] = actions

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, target: Surface):
        pass

    def on(self, event: str, *args, **kwargs):
        if event in self.actions:
            self.actions[event](*args, **kwargs)


class UIPanel(metaclass=ABCMeta):

    def __init__(self, game, visible: bool, rect: Rect, elements: list[UIElement]):
        self.game = game
        self.visible = visible
        self.rect: Rect = rect
        self.elements = elements

    def handle_input(self):
        if self.visible:
            for element in self.elements if self.visible else []:
                if element.rect.collidepoint(self.game.mouse_pos):
                    element.on("hover")
                else:
                    element.on("unhover")

            if MouseButtons.LEFT in self.game.mouse_btn_up:
                for element in self.elements if self.visible else []:
                    if element.rect.collidepoint(self.game.mouse_pos):
                        element.on("click")

            elif MouseButtons.RIGHT in self.game.mouse_btn_up:
                for element in self.elements if self.visible else []:
                    if element.rect.collidepoint(self.game.mouse_pos):
                        element.on("right_click")

            elif MouseButtons.MIDDLE in self.game.mouse_btn_up:
                for element in self.elements if self.visible else []:
                    if element.rect.collidepoint(self.game.mouse_pos):
                        element.on("middle_click")

    def update(self):
        for element in self.elements if self.visible else []:
            element.update()

    def render(self):
        for element in self.elements if self.visible else []:
            element.render(self.game.screen)

