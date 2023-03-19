import pygame
from pygame import Rect


class SpriteSheet:
    def __init__(self, filename: str):
        self.sheet = pygame.image.load(filename).convert_alpha()

    def sprite(self, rect: Rect):
        rect = pygame.Rect(rect)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)

        return image

    def sprites(self, rects: dict[str, Rect]):
        sprites = {}
        for name, rect in rects.items():
            sprites[name] = self.sprite(rect)

        return sprites
