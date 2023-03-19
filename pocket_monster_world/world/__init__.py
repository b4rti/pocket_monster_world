

class World:
    def __init__(self):
        self.chunks: dict[tuple[int, int], Chunk] = {}


class Chunk:
    def __init__(self):
        self.loaded: bool = False
        self.active: bool = False
        self.tiles: dict[tuple[int, int], Tile] = {}


class Tile:
    def __init__(self):
        pass


class Entity:
    def __init__(self):
        pass

