# Linguistic Game  

## Overview
**Linguistic Game** is a turn-based text-based game where the player navigates through a grid, encounters enemies, and engages in battles using a word-based combat system. The game features dynamic map generation and interactive gameplay, providing a unique experience with each playthrough.

## Features
* **Dynamic Map Generation:** Create a grid-based map with barriers, enemies, and player positions.
* **Combat System:** Engage enemies in battle using a word-based system where the number of vowels in the input word affects the outcome.
* **Interactive Gameplay:** Move around the grid, encounter enemies, and interact with barriers.

## Installation
1. **Clone the repository**: 
```
git clone https://github.com/yourusername/linguistic_game.git
```

2. **Navigate to the project directory**:  
```
cd linguistic_game
```

3. **Install any required dependencies (if applicable)**.
```
pip install -r requirements.txt
```

## Usage  
1. Ensure you have Python 3.x installed.

2. Run the game by executing:
```
python linguistic_game/main.py 
```

3. Follow the on-screen prompts to navigate, fight enemies, and enjoy the game.

## Project Structure

```markdown
📁 project-root
├── 📁 config
│ ├── 📄 __init__.py
│ └── 📄 constants.py
│
├── 📁 src
│ ├── 📄 __init__.py
│ ├── 📄 gameplay.py
│ ├── 📄 mechanics.py
│ └── 📄 map_utils.py
│
├── 📄 .gitignore
├── 📄 .gitattributes
└── 📄 main.py
```

* **config/**: Contains configuration files.
  * ***\__init__.py***: Imports constants for game configuration.
  * ***constants.py***: Defines constants used throughout the game.

* **src/**: Containts source code files.
  * ***\__init__.py***: Initializes the source package and sets up logging.
  * ***gameplay.py***: Contains functions for printing the game state and counting enemies.
  * ***mechanics.py***: Handles player movement and combat mechanics.
  * ***map_utils.py***: Provides functions for generating and placing entities on the map.

* **.gitignore**: Specifies files and directories to be ignored by Git (e.g., virtual environments, build artifacts).
* **.gitattributes**: Ensures consistent line endings across different operating systems in the repository.
* * **main.py**: The entry point of the game. It initializes game settings, generates the map, places entities, and starts the game loop. It handles player movement, enemy encounters, and displays the game state.

## Code Example

* **Map Generation**: Uses `get_map` to initialize a grid filled with spaces.
* **Entity Placement**: `enemurate_amounts` assigns entities to random coordinates.
* **Movement**: `make_movement` handles user input for moving and fighting.
* **Combat**: `fight` resolves battles based on vowel counts in user input.
  
### Main Game Loop
```python
from config.constants import (
  HEALTH_CONSTANT, SIZE_CONSTANT, AMOUNT_CONSTANTS,
  ENTITY_CONSTANTS, SPATIAL_CONSTANTS, TEXT_DIR, TEXT_F_NAME
)

from src.gameplay import print_game, count_enemies
from src.map_utils import get_map, read_print_intro, enumerate_amounts, place_entities
from src.mechanics import make_movement

def main():
    health = HEALTH_CONSTANT
    size = SIZE_CONSTANT
    amounts = AMOUNT_CONSTANTS
    entities = ENTITY_CONSTANTS
    spatials = SPATIAL_CONSTANTS
    text_dir = TEXT_DIR
    text_f_name = TEXT_F_NAME

    my_empty_map = get_map(spatials, size)
    my_entities, my_player_coords = enumerate_amounts(entities, amounts, size)
    my_game_map = place_entities(my_entities, my_empty_map)

    # Start the game
    read_print_intro(text_dir, text_f_name)
    print_game(health, my_game_map)
    while health > 0:
        my_player_coords, my_game_map, health = make_movement(
            health=health,
            spatials=spatials,
            size=size,
            game_map=my_game_map,
            old_coords=my_player_coords,
            entities=entities
        )
        print_game(health, my_game_map)
        # Check enemy amount. If zero, raise win message.
        if count_enemies(my_game_map, entities['enemy']) == 0:
            print("Congratulations! You have defeated all the enemies!")
            break
        # Check whether health is lower than zero. If yes, raise lose message.
        if health <= 0:
            print("Game over. You have already lost all of your precious health...")

if __name__ == "__main__":
    main()

```

For the complete code, check out the [main.py file](https://github.com/kgordu/linguistic_game/blob/main/main.py) in the repository.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](https://github.com/kivanc57/linguistic_game/blob/main/LICENSE) file for details.



## Contact
Let me know if there are any specific details you’d like to adjust or additional sections you want to include!  
* **Email**: kivancgordu@hotmail.com
* **Version**: 1.0.0
* **Date**: 22-06-2024
