from random import randint

def make_movement(health, spatials, size, game_map, old_coords, entities):
    # Make a movement based on the user's input direction
    moves = {
        'W' : (old_coords[0] - 1, old_coords[1]),
        'S' : (old_coords[0] + 1, old_coords[1]),
        'D' : (old_coords[0], old_coords[1] + 1),
        'A' : (old_coords[0], old_coords[1] - 1)
    }
    direct_msg = (
        "Now, please kindly enter a direction accordingly to the instructions.\n"
        ">Direction I wanna go(WASD): "
        )
    try:
        given_direct = input(direct_msg + " \t").upper()
        if given_direct not in moves:
            raise ValueError("Invalid direction. Please enter a new one: ")

        new_coords = moves[given_direct]

        # Check the given direction.
        # Give an error in case of violation of borders or attempts onto barriers.
        # If enemy is located, started to fight.
        # If none of these above, move to that direction.
        
        if not (0 <= new_coords[0] < size) and (0 <= new_coords[1] < size):
            raise ValueError(f"Move out of bonds. Try again.")
        cell_value = game_map[new_coords[0]][new_coords[1]]
        if cell_value == entities['barrier']:
            print("You bumped into a barrier. Try again.")
            return old_coords, game_map, health
        elif cell_value == entities['enemy']:
            print("You encountered an ENEMY!!!")
            game_map, health = fight(game_map, health)
            if health > 0:
                game_map[old_coords[0]][old_coords[1]] = spatials['space']
                game_map[new_coords[0]][new_coords[1]] = entities['player']
                return new_coords, game_map, health
            else:
                return old_coords, game_map, health
        else:
            game_map[old_coords[0]][old_coords[1]] = spatials['space']
            game_map[new_coords[0]][new_coords[1]] = entities['player']
            return new_coords, game_map, health
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return old_coords, game_map, health

def fight(game_map, health):
    try:
        count_vowels = 0
        magic_number = randint(1, 6)
        vowel_set = set('aeiou')
        print("Oi! It is time to fight!")
        magic_word = input("Spell the magic words: ")
        count_vowels = sum(1 for letter in magic_word.lower() if letter in vowel_set)
        while (count_vowels != magic_number) and (health > 0):
            count_vowels = sum(1 for letter in magic_word.lower() if letter in vowel_set)
            damage = abs(magic_number - count_vowels) * 6
            health -= damage
            if health <= 0:
                print("You Lost. You are out of health...")
                return game_map, health
            print(f"Health: {health}\n")
            print(f"You missed! You took {damage} damage.\n")
            magic_word = input("Try again. Give me another one: ")
            count_vowels = sum(1 for letter in magic_word.lower() if letter in vowel_set)
            if count_vowels == magic_number:
                print("You defeated the enemy!!")
                return game_map, health
    
    except Exception as e:
        print(f"An error occurred during this fight: {e}")
        return game_map, health
