from pocket_monster_world.game_state import GameState


class WorldState(GameState):
    name = "world"

    def __init__(self, game):
        super().__init__(game)

    def handle_input(self):
        pass

    def update(self):
        pass

    def shadow_update(self):
        pass

    def render(self):
        pass

    def shadow_render(self):
        pass

    def on_enter(self):
        pass

    def on_exit(self):
        pass
