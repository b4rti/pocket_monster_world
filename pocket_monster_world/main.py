from pocket_monster_world.game import Game
from pocket_monster_world.state.intro import IntroState


def main():
    game = Game()
    game.states.push(IntroState(game))
    game.run()


if __name__ == '__main__':
    main()
