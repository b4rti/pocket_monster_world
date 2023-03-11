from pocket_monster_world.game.plugin import Plugin


class ExamplePlugin(Plugin):
    name = "Example Plugin"
    description = "An example plugin"
    version = "1.0.0"

    def on_enable(self):
        # print("Example plugin enabled")
        pass

    def on_disable(self):
        # print("Example plugin disabled")
        pass

    def handle_input(self):
        # print("Example plugin input")
        pass

    def pre_update(self):
        # print("Example plugin pre update")
        pass

    def post_update(self):
        # print("Example plugin post update")
        pass

    def pre_render(self):
        # print("Example plugin pre render")
        pass

    def post_render(self):
        # print("Example plugin post render")
        pass
