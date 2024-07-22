from config.constants import (
  HEALTH_CONSTANT, SIZE_CONSTANT, AMOUNT_CONSTANTS,
  ENTITY_CONSTANTS, SPATIAL_CONSTANTS, TEXT_DIR, TEXT_F_NAME
)

from game_module.gameplay import print_game, count_enemies
from game_module.map_utils import get_map, read_print_intro, enumerate_amounts, place_entities
from game_module.mechanics import make_movement

def main():
    health = HEALTH_CONSTANT
    size = SIZE_CONSTANT
    amounts = AMOUNT_CONSTANTS
    entities = ENTITY_CONSTANTS
    spatials = SPATIAL_CONSTANTS
    text_dir = TEXT_DIR
    text_f_name = TEXT_F_NAME

    my_empty_map = get_map (spatials,  size)
    my_entities, my_player_coords = enumerate_amounts(entities, amounts, size)
    my_game_map = place_entities(my_entities, my_empty_map)

    #Start the game
    read_print_intro(text_dir, text_f_name)
    print_game(health, my_game_map)
    while health > 0:
        my_player_coords, my_game_map, health = \
            make_movement(
                health=health,
                spatials=spatials,
                size=size,
                game_map=my_game_map,
                old_coords=my_player_coords,
                entities=entities
                )
        print_game(health, my_game_map)
        #Check enemy amount. If zero, raise win message.
        if count_enemies(my_game_map, entities['enemy']) == 0:
            print("Congratulations! You have defeated all the enemies!")
            break
        #Check whether health is lower than zero. If yes, raise loose message.
        if health <= 0:
            print("Game over. You have already lost all of your precious health...")

if __name__ == "__main__":
    main()
