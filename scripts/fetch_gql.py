import json

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


def run():
    transport = AIOHTTPTransport(url="https://beta.pokeapi.co/graphql/v1beta")

    client = Client(transport=transport, fetch_schema_from_transport=True)

    query = gql(
        """
        query getPokemon {
          pokemon_v2_pokemon(where: {id: {_eq: 1}}) {
            id
            name
            pokemon_v2_pokemonabilities {
              pokemon_v2_ability {
                id
                name
              }
            }
          }
        }
        """
    )

    result = client.execute(query)
    print(json.dumps(result, indent=2))


'''
query getPokemon {
  pokemon_v2_pokemon(limit: 3) {
    id
    name
    pokemon_v2_pokemonabilities {
      pokemon_v2_ability {
        name
      }
    }
    pokemon_v2_pokemonmoves(limit: 3) {
      pokemon_v2_move {
        name
      }
    }
    pokemon_v2_pokemonstats {
      id
      stat_id
      base_stat
      effort
      pokemon_v2_stat {
        id
        name
      }
    }
  }
}

query getMoves {
  pokemon_v2_move(limit: 10) {
    id
    name
    pokemon_v2_moveeffect {
      pokemon_v2_moveeffecteffecttexts {
        short_effect
        effect
      }
    }
  }
}

query getItems {
  pokemon_v2_item(limit: 10) {
    id
    name
    cost
    fling_power
    pokemon_v2_itemcategory {
      id
      name
    }
    pokemon_v2_itemeffecttexts {
      short_effect
      effect
    }
  }
}

query getBerries {
  pokemon_v2_berry(limit: 10) {
    id
    name
    growth_time
    max_harvest
    size
    smoothness
    soil_dryness
    pokemon_v2_type {
      name
    }
    pokemon_v2_item {
      id
      name
      cost
      fling_power
      pokemon_v2_itemeffecttexts {
        short_effect
        effect
      }
    }
  }
}

query getEncounter {
  pokemon_v2_encounter(limit: 10, offset: 110) {
    pokemon_v2_pokemon {
      name
    }
    min_level
    max_level
    pokemon_v2_locationarea {
      name
    }
    pokemon_v2_encounterslot {
      slot
      rarity
    }
  }
}
'''
