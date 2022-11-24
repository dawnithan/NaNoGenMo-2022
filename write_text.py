import pokebase as pb
import random
import json
import math

# https://pokeapi.co/docs/v2#pokemon-species

filename = './pkmn-adventure-generator/output.txt'
# NUM_ENTRIES = 10
caught = []
seen = []

# Stats
num_pokedex_checked = 0
num_pokemon_missed = 0
num_pokemon_caught = 0
num_pokecentre_trips = 0
num_pokemart_trips = 0
num_caves = 0
num_forests = 0
num_routes = 0

with open('./pkmn-adventure-generator/reactions.txt', 'r', encoding='utf-8') as file:
    responses = [f.strip() for f in file.readlines()]

with open('./pkmn-adventure-generator/pokedata.json', 'r') as data:
    pokedata = json.load(data)

def clear_output():
    open(filename, 'w').close()

def check_pokedex():
    global num_pokedex_checked
    output = ''
    output += '> Time to check in with my POKéDEX progress. How many POKéMON have I caught versus how many I\'ve seen?\n'
    output += f'According to my POKéDEX, out of {len(pokedata)} POKéMON in the region, I have SEEN {len(seen)} POKéMON and of that number I have CAUGHT {len(caught)} POKéMON.\n'
    output += f'That is {math.floor((len(seen) / len(pokedata)) * 100)}% of the way there in terms of POKéMON SEEN!\n'
    output += f'A quick look inside my PC boxes show the following list of POKéMON that I have CAUGHT:\n\n'
    for c in caught:
        output += f'\t* {c}\n'
    num_pokedex_checked += 1
    return output

def template_caught_1(name, level, ability, moves, flavor_text, nature):
    response = random.choice(responses)
    output = ''
    output += f'> I found {name}! It appears to be Lv. {level} with the moves {moves[0].upper()}, {moves[1].upper()}, {moves[2].upper()}, and {moves[3].upper()}\n'
    output += f'It has a {nature} nature, with the ability {ability}.\n'
    output += f'Here\'s what the POKéDEX has to say about it:\n'
    output += f'* {flavor_text[0]}\n'
    output += f'So {response}!\n'
    return output

def template_caught_2(name, level, ability, moves, flavor_text, nature):
    response = random.choice(responses)
    output = ''
    output += f'> Hey, look what I caught - {name}! It\'s got quite a {nature} nature.\n'
    output += f'According to my POKéDEX, it\'s Lv. {level} and knows {moves[0].upper()}, {moves[1].upper()}, {moves[2].upper()}, and {moves[3].upper()}\n'
    output += f'Nice, its ability is {ability}!\n'
    output += f'The description from the POKéDEX states:\n'
    output += f'* {flavor_text[0]}\n'
    output += f'{response[0].upper() + response[1:]} find!\n'
    return output

def template_caught_3(name, level, ability, moves, flavor_text, nature):
    response = random.choice(responses)
    output = ''
    output += f'> Whoa, you won\'t believe it; I stumbled across {name}! And it\'s got the ability {ability}!\n'
    output += f'Apparently it is Lv. {level} and has a {nature} nature. Seems to know {moves[0].upper()}, {moves[1].upper()}, {moves[2].upper()}, and {moves[3].upper()}!\n'
    output += f'Oh, and here\'s what the POKéDEX says:\n'
    output += f'* {flavor_text[0]}\n'
    output += f'Score! Just {response}.\n'
    return output

def template_missed_capture(name):
    options = [
        '> Shoot! I nearly caught a {0}, but it got away. Better luck next time...\n',
        '> Aw, I found a {0} but it managed to slip away. It looked strong, too...\n',
        '> Despite my best efforts, I wasn\'t able to catch that {0}... Hopefully I find another one!\n'
    ]
    choice = random.choice(options)
    # num_pokemon_missed += 1
    return choice.format(name.upper())

def template_move_activity():
    global num_pokecentre_trips
    global num_pokemart_trips
    global num_caves
    global num_forests
    global num_routes
    options = [
        '> I decided to go back to the nearest POKéCENTRE and heal up the team. Time to refresh!\n',
        '> I went to the POKéMART to stock back up on potions and POKéBALLS. Always be prepared!\n',
        '> I decided to enter a forest on a nearby route to look for new POKéMON. So eerie...\n',
        '> I ended up looking inside a damp, dark cave for new POKéMON. Should\'ve brought an escape rope!\n',
        '> I took a stroll down a nice route full of people and POKéMON - I love the fresh, crisp air!\n'
    ]
    choice = random.choice(options)
    which = options.index(choice)
    match (which):
        case 0: num_pokecentre_trips += 1
        case 1: num_pokemart_trips += 1
        case 2: num_forests += 1
        case 3: num_caves += 1
        case 4: num_routes += 1
    return choice

def template_starter(name, level, ability, moves, flavor_text, nature):
    output = ''
    output += f'> The meeting with the professor went great! There were tons of POKéMON on offer but I eventually settled on one that caught my eye: {name}!\n'
    output += f'Naturally, it\'s Lv. {level} and already has the moveset {moves[0].upper()}, {moves[1].upper()}, {moves[2].upper()}, and {moves[3].upper()}.\n'
    output += 'I wonder where the professor found something like this? Whatever, it\'s gotta be strong!\n'
    output += f'According to them, my {name} has a {nature} nature and the ability {ability}. That\'ll definitely come in handy.\n'
    output += f'Oh, I was also given a POKéDEX! This is what it had to say about my {name}:\n'
    output += f'* {flavor_text[0]}\n'
    output += f'I can\'t wait to see what else I\'ll learn about POKéMON with this! The professor gave me a ton of POKéBALLS so I should be good to go.\n'
    return output

def introduction():
    intro_text = ''
    intro_text += '> Today, I am beginning my adventure as a POKéMON TRAINER! I\'m excited to begin my journey and attempt to complete my POKéDEX!\n'
    intro_text += 'I\'m off to the professor to get my starter - I hope it will be a cute one!\n'
    intro_text += 'Oh, and also, I will document my daily activities here in this document. By the end of my trip, I\'m sure to be a POKéMON master, right?\n'
    intro_text += 'Alright, let\'s go!\n\n' 
    return intro_text

def ending():
    # num_pokemon_caught = len(caught)
    output = ''
    output += f'Phew, time to take a break! I got quite a lot done, wouldn\'t you say?\n'
    output += f'Did I manage to become a POKéMON master? Let\'s take a look at the stats:\n\n'
    output += f'Times I checked the POKéDEX: {num_pokedex_checked}\n'
    output += f'Trips to the POKéCENTRE: {num_pokecentre_trips}\n'
    output += f'Trips to the POKéMART: {num_pokemart_trips}\n'
    output += f'Forests entered: {num_forests}\n'
    output += f'Caves entered: {num_caves}\n'
    output += f'Routes entered: {num_routes}\n\n'
    output += f'And of course, time to look at the results of the POKéDEX...\n\n'
    output += f'According to my POKéDEX, out of {len(pokedata)} POKéMON in the region, I have SEEN {len(seen)} POKéMON and of that number I have CAUGHT {len(caught)} POKéMON.\n'
    output += f'So in total, I got {math.floor((len(seen) / len(pokedata)) * 100)}% of the way there in terms of POKéMON SEEN.\n'
    output += 'Not bad!\n'
    output += f'My final PC boxes show the following list of POKéMON that I have CAUGHT:\n\n'
    for c in caught:
        output += f'\t* {c}\n'
    output += '\n'
    output += f'Well, thank you for joining me on this adventure! I wonder what the next one will be like?'
    return output

def mudkip():
    output = '\n\n\n\n'
    output += 'ERROR: POKéDEX OVERLOAD.\n'
    num = random.randint(24, 999)
    for i in range(num):
        if (i % 12 == 0):
            output += '\n'
        output += 'mudkip '
    output += '...'
    return output

def write():
    with open(filename, 'a', encoding='utf-8') as result:
        # Clear the old output.txt
        clear_output()
        
        # Shuffle the Pokémon data
        random.shuffle(pokedata)
    
        # Write the introduction
        intro = introduction()
        result.write(intro)

        # For each Pokémon in the list, create an entry for it.
        # Then, roll a chance to write an activity to the output
        # Each activity has a chance to also cause another activity
        index = 0
        entries = 0
        while (len(seen) < len(pokedata)):
            poke_dict = json.loads(pokedata[index])
            
            name = poke_dict['name'].upper()
            level = poke_dict['level']
            ability = poke_dict['ability'].upper()
            moves = poke_dict['moves']
            flavor_text = poke_dict['flavor_text']
            nature = poke_dict['nature']

            # If this is the first Pokémon, use the Starter template
            if (entries <= 0):
                out = template_starter(name=name, level=level, ability=ability, moves=moves, flavor_text=flavor_text, nature=nature)
                seen.append(name)
                caught.append(f'Lv. {level} {name} - {ability} and {nature} nature.')
                index += 1
            # Post a Pokédex update
            elif (entries % 25 == 0):
                out = check_pokedex()
            else:
                # Decide which template to use
                roll = random.random()

                # 80% to encounter a Pokémon
                if (roll < 0.8):
                    seen.append(name)
                    catch_roll = random.random()
                    # 90% to catch it
                    if (catch_roll < 0.9):
                        caught.append(f'Lv. {level} {name} - {ability} and {nature} nature.')
                        templates = [0, 1, 2]
                        choice = random.choice(templates)
                        match (choice):
                            case 0: out = template_caught_1(name=name, level=level, ability=ability, moves=moves, flavor_text=flavor_text, nature=nature)
                            case 1: out = template_caught_2(name=name, level=level, ability=ability, moves=moves, flavor_text=flavor_text, nature=nature)
                            case 2: out = template_caught_3(name=name, level=level, ability=ability, moves=moves, flavor_text=flavor_text, nature=nature)
                    else:
                        out = template_missed_capture(name=name)
                    print(f'Wrote entry {name} to output. ({index})')
                    index += 1
                else:
                    out = template_move_activity()
            out += '\n'
            result.write(out)
            entries += 1
        result.write(ending())
        result.write(mudkip())
        
    
if __name__ == "__main__":
    write()
    print(f'Pokemon in pokedata: {len(pokedata)}')
    print(f'Pokemon in seen: {len(seen)}')