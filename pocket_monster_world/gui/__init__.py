

class GuiManager:
    def __init__(self, game: 'Game'):
        self.game = game

    def __getattr__(self, item):
        pass

    def handle_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass
