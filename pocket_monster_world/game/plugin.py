import importlib
import os

from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):
    name: str
    description: str
    version: str

    def __init__(self, game: 'Game'):
        self.game = game

    @abstractmethod
    def on_enable(self):
        pass

    @abstractmethod
    def on_disable(self):
        pass

    @abstractmethod
    def handle_input(self):
        pass

    @abstractmethod
    def pre_update(self):
        pass

    @abstractmethod
    def post_update(self):
        pass

    @abstractmethod
    def pre_render(self):
        pass

    @abstractmethod
    def post_render(self):
        pass


class PluginManager:

    def __init__(self, game: 'Game'):
        self.game = game
        self.plugins = []

    def __getattr__(self, item):
        for plugin in self.plugins:
            if plugin.name == item:
                return plugin

    def load(self, plugin_name: str):
        package_path = f"plugins.{plugin_name}"
        class_name = f"{plugin_name.title().replace('_', '')}Plugin"

        try:
            package = importlib.import_module(package_path)
            class_ = getattr(package, class_name)
            plugin = class_(self.game)
            plugin.on_enable()
            self.plugins.append(plugin)
        except Exception as e:
            print(f"Failed to load plugin {plugin_name}: {e}")

    def load_all(self):
        plugins_dirs = [plugin_dir.name for plugin_dir in os.scandir("plugins") if
                        plugin_dir.is_dir() and not plugin_dir.name.startswith("_")]
        for plugin_dir in plugins_dirs:
            print(f"Loading plugin: {plugin_dir}")
            self.load(plugin_dir)

    def unload(self, plugin: Plugin):
        print(f"Unloading plugin: {plugin.name}")
        try:
            plugin.on_disable()
        except Exception as e:
            print(f"Failed to unload plugin {plugin.name}: {e}")
        self.plugins.remove(plugin)

    def unload_all(self):
        for plugin in self.plugins:
            self.unload(plugin)

    def reload(self, plugin: Plugin):
        print(f"Reloading plugin: {plugin.name}")
        try:
            self.unload(plugin)
        except Exception as e:
            print(f"Failed to reload plugin {plugin.name}: {e}")
        self.load(plugin.name)

    def reload_all(self):
        for plugin in self.plugins:
            self.reload(plugin)

    def handle_input(self):
        for plugin in self.plugins:
            try:
                plugin.handle_input()
            except Exception as e:
                print(f"Failed to handle input for plugin {plugin.name}: {e}")

    def pre_update(self):
        for plugin in self.plugins:
            try:
                plugin.pre_update()
            except Exception as e:
                print(f"Failed on pre update for plugin {plugin.name}: {e}")

    def post_update(self):
        for plugin in self.plugins:
            try:
                plugin.post_update()
            except Exception as e:
                print(f"Failed on post update for plugin {plugin.name}: {e}")

    def pre_render(self):
        for plugin in self.plugins:
            try:
                plugin.pre_render()
            except Exception as e:
                print(f"Failed on pre render for plugin {plugin.name}: {e}")

    def post_render(self):
        for plugin in self.plugins:
            try:
                plugin.post_render()
            except Exception as e:
                print(f"Failed on post render for plugin {plugin.name}: {e}")
