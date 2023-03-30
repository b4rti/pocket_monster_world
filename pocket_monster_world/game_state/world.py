import numpy as np
import pygame
from noise import pnoise2

from pygame import Surface, Rect

from pocket_monster_world.game_state import GameState
from pocket_monster_world.sprite import SpriteSheet


class WorldState(GameState):
    name = "world"

    def __init__(self, game):
        super().__init__(game)
        self.spritesheet: SpriteSheet = SpriteSheet("assets/img/tiles/tileset.png")
        self.spritesheet2: SpriteSheet = SpriteSheet("assets/img/character/brendan.png")

        self.tiles_to_get = {
            "sand1": (1, 1, 16, 16),
            "sand2": (18, 1, 16, 16),
            "sand3": (35, 1, 16, 16),
            "sand4": (52, 1, 16, 16),
            "sand5": (69, 1, 16, 16),
            "sand6": (18, 18, 16, 16),
            "sand7": (35, 18, 16, 16),
            "sand8": (52, 18, 16, 16),
            "sand9": (69, 18, 16, 16),
            "sand10": (18, 35, 16, 16),
            "sand11": (35, 35, 16, 16),
            "sand12": (52, 35, 16, 16),
            "sand13": (69, 35, 16, 16),

            "gras1": (1, 52, 16, 16),
            "gras2": (18, 52, 16, 16),
            "gras3": (35, 52, 16, 16),
            "gras4": (52, 52, 16, 16),
            "gras5": (69, 52, 16, 16),
            "gras6": (18, 69, 16, 16),
            "gras7": (35, 69, 16, 16),
            "gras8": (52, 69, 16, 16),
            "gras9": (69, 69, 16, 16),
            "gras10": (18, 86, 16, 16),
            "gras11": (35, 86, 16, 16),
            "gras12": (52, 86, 16, 16),
            "gras13": (69, 86, 16, 16),

            "dirt1": (1, 103, 16, 16),
            "dirt2": (18, 103, 16, 16),
            "dirt3": (35, 103, 16, 16),
            "dirt4": (52, 103, 16, 16),
            "dirt5": (69, 103, 16, 16),
            "dirt6": (18, 120, 16, 16),
            "dirt7": (35, 120, 16, 16),
            "dirt8": (52, 120, 16, 16),
            "dirt9": (69, 120, 16, 16),
            "dirt10": (18, 137, 16, 16),
            "dirt11": (35, 137, 16, 16),
            "dirt12": (52, 137, 16, 16),
            "dirt13": (69, 137, 16, 16),

            "lawn1": (1, 154, 16, 16),
            "lawn2": (18, 154, 16, 16),
            "lawn3": (35, 154, 16, 16),
            "lawn4": (52, 154, 16, 16),
            "lawn5": (69, 154, 16, 16),
            "lawn6": (18, 171, 16, 16),
            "lawn7": (35, 171, 16, 16),
            "lawn8": (52, 171, 16, 16),
            "lawn9": (69, 171, 16, 16),
            "lawn10": (18, 188, 16, 16),
            "lawn11": (35, 188, 16, 16),
            "lawn12": (52, 188, 16, 16),
            "lawn13": (69, 188, 16, 16),

            "stone1": (1, 205, 16, 16),
            "stone2": (18, 205, 16, 16),
            "stone3": (35, 205, 16, 16),
            "stone4": (52, 205, 16, 16),
            "stone5": (69, 205, 16, 16),
            "stone6": (18, 222, 16, 16),
            "stone7": (35, 222, 16, 16),
            "stone8": (52, 222, 16, 16),
            "stone9": (69, 222, 16, 16),
            "stone10": (18, 239, 16, 16),
            "stone11": (35, 239, 16, 16),
            "stone12": (52, 239, 16, 16),
            "stone13": (69, 239, 16, 16),

            "cobble1": (1, 256, 16, 16),
            "cobble2": (18, 256, 16, 16),
            "cobble3": (35, 256, 16, 16),
            "cobble4": (52, 256, 16, 16),
            "cobble5": (69, 256, 16, 16),
            "cobble6": (18, 273, 16, 16),
            "cobble7": (35, 273, 16, 16),
            "cobble8": (52, 273, 16, 16),
            "cobble9": (69, 273, 16, 16),
            "cobble10": (18, 290, 16, 16),
            "cobble11": (35, 290, 16, 16),
            "cobble12": (52, 290, 16, 16),
            "cobble13": (69, 290, 16, 16),

            "paving1_1": (1, 307, 16, 16),
            "paving1_2": (18, 307, 16, 16),
            "paving1_3": (35, 307, 16, 16),
            "paving1_4": (52, 307, 16, 16),
            "paving1_5": (69, 307, 16, 16),
            "paving1_6": (18, 324, 16, 16),
            "paving1_7": (35, 324, 16, 16),
            "paving1_8": (52, 324, 16, 16),
            "paving1_9": (69, 324, 16, 16),

            "paving2_1": (18, 341, 16, 16),
            "paving2_2": (35, 341, 16, 16),
            "paving2_3": (52, 341, 16, 16),
            "paving2_4": (69, 341, 16, 16),
            "paving2_5": (86, 341, 16, 16),
            "paving2_6": (18, 358, 16, 16),
            "paving2_7": (35, 358, 16, 16),
            "paving2_8": (52, 358, 16, 16),
            "paving2_9": (69, 358, 16, 16),

            "paving3_1": (18, 375, 16, 16),
            "paving3_2": (35, 375, 16, 16),
            "paving3_3": (52, 375, 16, 16),
            "paving3_4": (69, 375, 16, 16),
            "paving3_5": (86, 375, 16, 16),
            "paving3_6": (18, 392, 16, 16),
            "paving3_7": (35, 392, 16, 16),
            "paving3_8": (52, 392, 16, 16),
            "paving3_9": (69, 392, 16, 16),

            "grave1": (1, 409, 16, 16),
            "grave2": (18, 409, 16, 16),
            "grave3": (35, 409, 16, 16),
            "grave4": (52, 409, 16, 16),
            "grave5": (69, 409, 16, 16),
            "grave6": (18, 426, 16, 16),
            "grave7": (35, 426, 16, 16),
            "grave8": (52, 426, 16, 16),
            "grave9": (69, 426, 16, 16),
            "grave10": (18, 443, 16, 16),
            "grave11": (35, 443, 16, 16),
            "grave12": (52, 443, 16, 16),
            "grave13": (69, 443, 16, 16),

            "beach1": (1, 460, 16, 16),
            "beach2": (18, 460, 16, 16),
            "beach3": (35, 460, 16, 16),
            "beach4": (52, 460, 16, 16),
            "beach5": (69, 460, 16, 16),
            "beach6": (18, 477, 16, 16),
            "beach7": (35, 477, 16, 16),
            "beach8": (52, 477, 16, 16),
            "beach9": (69, 477, 16, 16),
            "beach10": (18, 494, 16, 16),
            "beach11": (35, 494, 16, 16),
            "beach12": (52, 494, 16, 16),
            "beach13": (69, 494, 16, 16),

            "metal1": (1, 511, 16, 16),
            "metal2": (18, 511, 16, 16),
            "metal3": (35, 511, 16, 16),
            "metal4": (52, 511, 16, 16),
            "metal5": (69, 511, 16, 16),
            "metal6": (18, 528, 16, 16),
            "metal7": (35, 528, 16, 16),
            "metal8": (52, 528, 16, 16),
            "metal9": (69, 528, 16, 16),

            "water1": (188, 18, 16, 16),
        }

        self.tiles = self.spritesheet.sprites(self.tiles_to_get)

        self.character: Surface = self.spritesheet2.sprite(Rect(0, 0, 14, 21))

        self.surface: Surface = Surface((self.game.cfg.SCR_WIDTH, self.game.cfg.SCR_HEIGHT))
        self.surface.fill((255, 255, 255))

        noise_map = np.zeros((int(self.game.cfg.SCR_WIDTH / 16), int(self.game.cfg.SCR_HEIGHT / 16)))
        for x in range(int(self.game.cfg.SCR_WIDTH / 16)):
            for y in range(int(self.game.cfg.SCR_HEIGHT / 16)):
                noise_map[x][y] = pnoise2(x / 25, y / 25, octaves=2, persistence=0.25, lacunarity=4.0, repeatx=1024, repeaty=1024, base=0)

        for x in range(0, int(self.game.cfg.SCR_WIDTH / 16)):
            for y in range(0, int(self.game.cfg.SCR_HEIGHT / 16)):
                if noise_map[x][y] > 0.1:
                    self.surface.blit(self.tiles["water1"], (x * 16, y * 16))
                elif noise_map[x][y] > 0.0:
                    self.surface.blit(self.tiles["beach1"], (x * 16, y * 16))
                else:
                    self.surface.blit(self.tiles["gras1"], (x * 16, y * 16))



    def handle_input(self):
        pass

    def update(self):
        pass

    def shadow_update(self):
        pass

    def render(self):
        self.game.screen.blit(self.surface, (0, 0))


    def shadow_render(self):
        pass

    def on_enter(self):
        pygame.mixer.music.load("assets/midi/mus_rg_route1.mid")
        pygame.mixer.music.play(-1, 0.0, 2500)

    def on_exit(self):
        pass
