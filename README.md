![Logo](/assets/img/logo.png)

# Pocket Monster World (WIP)
[![Build](https://github.com/b4rti/pocket_monster_world/actions/workflows/package.yml/badge.svg)](https://github.com/b4rti/pocket_monster_world/actions/workflows/package.yml)

Pocket Monster World is a Pokémon RPG game made in Python using the Pygame-CE library.

![Screenshot](/assets/img/screenshot.png)

## Installation

### Poetry

```bash
pip install poetry
```

```bash
poetry install
```

## Usage

### Start the game directly

```bash
poetry run pmw
```

### Build the game executable

PyInstaller is used to build the game executable.

```bash
poetry run pip install pyinstaller
```

#### Windows

```bash
poetry run build
```

```bash
cd dist\pocket_monster_world && .\pocket_monster_world.exe
```

#### Linux / macOS

```bash
poetry run build
```
    
```bash
cd dist/pocket_monster_world && ./pocket_monster_world
```

### Download the latest release

[Release](https://github.com/b4rti/pocket_monster_world/releases/latest)

### Warning !

Due to the use of PyInstaller to build the game executable and the fact that the game executable is not signed,
it may be detected as a virus by some antivirus software.

`Linux` users should not be affected by this problem.

`Windows` users can add an exception to their antivirus software or start the game directly from the source code.

`MacOS` users should start the game directly from the source code.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Thanks

Thanks to [Pygame-CE](https://www.pyga.me/) for the game library.

Thanks to [rh-hideout](https://github.com/rh-hideout/pokeemerald-expansion/) for the Pokémon logic and MIDI files.

Thanks to [PokeAPI](https://pokeapi.co/) for the Pokémon data and sprites.
