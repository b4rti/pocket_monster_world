from abc import ABCMeta, abstractmethod


class GameState(metaclass=ABCMeta):
    name: str

    def __init__(self, game):
        self.game = game

    @abstractmethod
    def handle_input(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def shadow_update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def shadow_render(self):
        pass

    @abstractmethod
    def on_enter(self):
        pass

    @abstractmethod
    def on_exit(self):
        pass


class GameStateManager:
    def __init__(self, game):
        self.game = game
        self.states = []

    def __getattr__(self, item):
        for state in self.states:
            if state.name == item:
                return state

    def push(self, state: GameState):
        self.states.append(state)
        self.states[-1].on_enter()

    def pop(self):
        if self.states:
            self.states[-1].on_exit()
            self.states.pop()

    def change(self, state: GameState):
        self.pop()
        self.push(state)

    def handle_input(self):
        if self.states:
            self.states[-1].handle_input()

    def update(self):
        for state in self.states[:-1]:
            state.shadow_update()

        if self.states:
            self.states[-1].update()

    def render(self):
        for state in self.states[:-1]:
            state.shadow_render()

        if self.states:
            self.states[-1].render()
