import json
import os

import requests


# API_URL = 'https://pokeapi.co/api/v2'
API_URL = 'http://localhost/api/v2'


LIMIT = 9999
OFFSET = 0

FILTER = [
    'POKEMON',
    'ABILITIES',
    'BERRIES',
    'ITEMS',
    'MOVES',
    'NATURES',
    'SPECIES',
    'STATS',
    'TYPES',
]


def run():
    if 'POKEMON' in FILTER:
        print('Fetching Pokemon index...')
        pokemon_index_json = requests.get(f'{API_URL}/pokemon?limit={LIMIT}&offset={OFFSET}').json()['results']
        with open('assets/json/pokemon/index.json', 'w') as file:
            file.write(json.dumps(pokemon_index_json, indent=2))

        print('Fetching Pokemon data...')
        for pokemon in pokemon_index_json:
            print(f"Fetching {pokemon['name']}...")
            pokemon_json = requests.get(pokemon['url']).json()
            with open(f"assets/json/pokemon/{pokemon_json['name']}.json", 'w') as file:
                file.write(json.dumps(pokemon_json, indent=2))

            print(f"Fetching {pokemon['name']}'s sprites...")
            for sprite in ["front_default", "front_shiny", "front_female", "front_shiny_female",
                           "back_default", "back_shiny", "back_female", "back_shiny_female"]:
                if pokemon_json['sprites'][sprite]:
                    print(f"Fetching {pokemon['name']}'s {sprite} sprite...")
                    sprite_data = requests.get(pokemon_json['sprites'][sprite]).content
                    if not os.path.exists(f"assets/img/pokemon/{pokemon_json['name']}"):
                        os.mkdir(f"assets/img/pokemon/{pokemon_json['name']}")
                    with open(f"assets/img/pokemon/{pokemon_json['name']}/{sprite}.png", 'wb') as file:
                        file.write(sprite_data)

    if 'ABILITIES' in FILTER:
        print('Fetching Abilities index...')
        pokemon_abilities_json = requests.get(f'{API_URL}/ability?limit={LIMIT}&offset={OFFSET}').json()['results']
        with open('assets/json/abilities/index.json', 'w') as file:
            file.write(json.dumps(pokemon_abilities_json, indent=2))

        print('Fetching Abilities data...')
        for ability in pokemon_abilities_json:
            print(f"Fetching {ability['name']}...")
            ability_json = requests.get(ability['url']).json()
            with open(f"assets/json/abilities/{ability_json['name']}.json", 'w') as file:
                file.write(json.dumps(ability_json, indent=2))

    if 'BERRIES' in FILTER:
        print('Fetching Berries index...')
        pokemon_berries_json = requests.get(f'{API_URL}/berry?limit={LIMIT}&offset={OFFSET}').json()['results']
        with open('assets/json/berries/index.json', 'w') as file:
            file.write(json.dumps(pokemon_berries_json, indent=2))

        print('Fetching Berries data...')
        for berry in pokemon_berries_json:
            print(f"Fetching {berry['name']}...")
            berry_json = requests.get(berry['url']).json()
            with open(f"assets/json/berries/{berry_json['name']}.json", 'w') as file:
                file.write(json.dumps(berry_json, indent=2))

    if 'ITEMS' in FILTER:
        print('Fetching Items index...')
        pokemon_items_json = requests.get(f'{API_URL}/item?limit={LIMIT}&offset={OFFSET}').json()['results']
        with open('assets/json/items/index.json', 'w') as file:
            file.write(json.dumps(pokemon_items_json, indent=2))

        print('Fetching Items data...')
        for item in pokemon_items_json:
            print(f"Fetching {item['name']}...")
            item_json = requests.get(item['url']).json()
            with open(f"assets/json/items/{item_json['name']}.json", 'w') as file:
                file.write(json.dumps(item_json, indent=2))
            print(f"Fetching {item['name']}'s sprites...")
            for sprite in item_json['sprites']:
                if item_json['sprites'][sprite]:
                    print(f"Fetching {item['name']}'s {sprite} sprite...")
                    sprite_data = requests.get(item_json['sprites'][sprite]).content
                    with open(f"assets/img/items/{item_json['name']}_{sprite}.png", 'wb') as file:
                        file.write(sprite_data)

    if 'MOVES' in FILTER:
        print('Fetching Moves index...')
        pokemon_moves_json = requests.get(f'{API_URL}/move?limit={LIMIT}&offset={OFFSET}').json()['results']
        with open('assets/json/moves/index.json', 'w') as file:
            file.write(json.dumps(pokemon_moves_json, indent=2))

        print('Fetching Moves data...')
        for move in pokemon_moves_json:
            print(f"Fetching {move['name']}...")
            move_json = requests.get(move['url']).json()
            with open(f"assets/json/moves/{move_json['name']}.json", 'w') as file:
                file.write(json.dumps(move_json, indent=2))

    if 'NATURES' in FILTER:
        print('Fetching Natures index...')
        pokemon_natures_json = requests.get(f'{API_URL}/nature?limit={LIMIT}&offset={OFFSET}').json()['results']
        with open('assets/json/natures/index.json', 'w') as file:
            file.write(json.dumps(pokemon_natures_json, indent=2))

        print('Fetching Natures data...')
        for nature in pokemon_natures_json:
            print(f"Fetching {nature['name']}...")
            nature_json = requests.get(nature['url']).json()
            with open(f"assets/json/natures/{nature_json['name']}.json", 'w') as file:
                file.write(json.dumps(nature_json, indent=2))

    if 'SPECIES' in FILTER:
        print('Fetching Species index...')
        pokemon_species_json = requests.get(f'{API_URL}/pokemon-species?limit={LIMIT}&offset={OFFSET}').json()['results']
        with open('assets/json/species/index.json', 'w') as file:
            file.write(json.dumps(pokemon_species_json, indent=2))

        print('Fetching Species data...')
        for species in pokemon_species_json:
            print(f"Fetching {species['name']}...")
            species_json = requests.get(species['url']).json()
            with open(f"assets/json/species/{species_json['name']}.json", 'w') as file:
                file.write(json.dumps(species_json, indent=2))

    if 'STATS' in FILTER:
        print('Fetching Stats index...')
        pokemon_stats_json = requests.get(f'{API_URL}/stat?limit={LIMIT}&offset={OFFSET}').json()['results']
        with open('assets/json/stats/index.json', 'w') as file:
            file.write(json.dumps(pokemon_stats_json, indent=2))

        print('Fetching Stats data...')
        for stat in pokemon_stats_json:
            print(f"Fetching {stat['name']}...")
            stat_json = requests.get(stat['url']).json()
            with open(f"assets/json/stats/{stat_json['name']}.json", 'w') as file:
                file.write(json.dumps(stat_json, indent=2))

    if 'TYPES' in FILTER:
        print('Fetching Types index...')
        pokemon_types_json = requests.get(f'{API_URL}/type?limit={LIMIT}&offset={OFFSET}').json()['results']
        with open('assets/json/types/index.json', 'w') as file:
            file.write(json.dumps(pokemon_types_json, indent=2))

        print('Fetching Types data...')
        for type in pokemon_types_json:
            print(f"Fetching {type['name']}...")
            type_json = requests.get(type['url']).json()
            with open(f"assets/json/types/{type_json['name']}.json", 'w') as file:
                file.write(json.dumps(type_json, indent=2))
