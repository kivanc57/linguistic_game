def print_game(health, game_map) :
    for row in game_map:
        print(" ".join(row))
    print(f"Health: {health}")

def count_enemies(game_map, enemy_symbol):
    return sum(row.count(enemy_symbol) for row in game_map)
