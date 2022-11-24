import pokebase as pb
import json
import random
import time
from os import path

# filename = './pkmn-adventure-generator/pokedata.json'
filename = './pkmn-adventure-generator/pokedata-2.json'
natures = [
    'HARDY','LONELY','ADAMANT','NAUGHTY','BRAVE',
    'BOLD','DOCILE','IMPISH','LAX','RELAXED','MODEST',
    'MILD','BASHFUL','RASH','QUIET','CALM','GENTLE',
    'CAREFUL','QUIRKY','SASSY','TIMID','HASTY','JOLLY',
    'NAIVE','SERIOUS'
]
pokemon = []

class Poke:
    def __init__(self, name, level, ability, moves, flavor_text, nature) -> None:
        self.name = name 
        self.level = level
        self.ability = ability
        self.moves = moves
        self.flavor_text = flavor_text,
        self.nature = nature

# Get a list of Pokémon from a specific region
# pokedex = pb.pokedex('hoenn')
pokedex = pb.pokedex('kanto')
entries = pokedex.pokemon_entries

entries_test = ['deoxys']

# For each Pokémon in that region, look up its details
with open(filename, 'w+') as json_file:
    for entry in entries:
        # s_entry = entry
        s_entry = str(entry.pokemon_species)
        print(s_entry + ' - processing')
        
        ps = pb.pokemon_species(s_entry)
        p = pb.pokemon(s_entry)

        # Get flavour text
        for t in ps.flavor_text_entries:
            if(str(t.language) == 'en'):
                p_text = t.flavor_text

        # Get ability
        try:
            p_ability = str(random.choice(p.abilities).ability)
        except:
            p_ability = "UNKNOWN"
            print("No ability found - skipping")

        # Get moves
        try:
            full_moves = p.moves
            p_moves = []
            for i in range(4):
                p_moves.append(str(random.choice(full_moves).move).upper())
        except:
            p_moves = ['???', '???', '???', '???']
            print("No moves found - skipping")
        
        # Get level
        p_level = random.randint(1, 100)

        # Get nature
        p_nature = random.choice(natures)

        new_poke = Poke(s_entry, p_level, p_ability, p_moves, p_text, p_nature)
        
        # Clear the file and then write the latest copy of the list to it
        json_file.truncate(0)
        json_file.seek(0)
        pokemon.append(json.dumps(new_poke.__dict__))
        json.dump(pokemon, json_file, indent=4, separators=(',',': '))
        # json_file.write(json.dumps(new_poke.__dict__))
        
        # Wait 3 seconds to avoid rate limit
        print(s_entry + ' - done')
        time.sleep(3)

# pokemon_json = []
# for p in pokemon:
#     p_json = json.dumps(p.__dict__)
#     print(p_json)
#     pokemon_json.append(p_json)