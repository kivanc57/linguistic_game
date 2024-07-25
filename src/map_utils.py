from random import randint
from os.path import dirname, join, abspath

def get_map (spatials, size):
# Get a map filled with 'space' constant
    return [[spatials['space']] * size for _ in range(size)]

def assign_coords(max_coord):
    # Assign random coordinates up to max_coord which is the size of a line.
    # This helper function soon to be used in enumerate_amounts function.
    return (randint(1, max_coord - 1), randint(1, max_coord - 1))

def read_print_intro(intro_text_dir, intro_text_file):
    # Read and print game introduction
    try:
        project_dir = dirname(abspath(__file__))
        full_path = join(project_dir, intro_text_dir, intro_text_file)
        with open(full_path, mode='r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print("Introduction text not found.")
    except Exception as e:
        print(f"An error occurred while trying to read the introduction: {e}")

def enumerate_amounts(entity_symbols, entity_constants, max_coord):
    # Enumerate each entity and assign them a random 2-D coordinates tuple.
    # Check whether there is a duplicate.
    # If yes, reassign the entity's coordinates.
    coords_dict = dict()
    coords_set = set()

    for entity, symbol in entity_symbols.items():
        if symbol not in coords_dict.keys():
            coords_dict[symbol] = list()

        min_amount, max_amount = entity_constants[entity][0], entity_constants[entity][1]
        amount = randint(min_amount, max_amount)

        for _ in range(amount):
            temp_coords = assign_coords(max_coord)
            while temp_coords in coords_set:
                temp_coords = assign_coords(max_coord)
            coords_dict[symbol].append(temp_coords)
            coords_set.add(temp_coords)
            if entity == 'player':
                player_coords = temp_coords
    return coords_dict, player_coords

def place_entities(coords_dict, game_map):
    # Place each entity's symbol on the assigned coordinates on the map
    for symbol, coords in coords_dict.items():
        for (x, y) in coords:
            game_map[x][y] = symbol
    return game_map
