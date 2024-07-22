# Linguistic Game  

## Overview
**Linguistic Game** is a turn-based text-based game where the player navigates through a grid, encounters enemies, and engages in battles using a word-based combat system. The game features dynamic map generation and interactive gameplay, providing a unique experience with each playthrough.

## Features
* **Dynamic Map Generation:** Create a grid-based map with barriers, enemies, and player positions.
* **Combat System:** Engage enemies in battle using a word-based system where the number of vowels in the input word affects the outcome.
* **Interactive Gameplay:** Move around the grid, encounter enemies, and interact with barriers.

## Installation
1. Clone the repository:  
`git clone https://github.com/yourusername/linguistic_game.git`

2. Navigate to the project directory:  
`cd linguistic_game`

3. Install any required dependencies (if applicable).

## Usage  
1. Ensure you have Python 3.x installed.

2. Run the game by executing:
`python linguistic_game/main.py`  

3. Follow the on-screen prompts to navigate, fight enemies, and enjoy the game.

## Project Structure
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

## Code Example
* **Map Generation**: Uses **get_map** to initialize a grid filled with spaces.
* **Entity Placement**: **enumerate_amounts** assigns entities to random coordinates.
* **Movement**: **make_movement** handles user input for moving and fighting.
* **Combat**: **fight** resolves battles based on vowel counts in user input.

## Code Example
**main.py**: The entry point of the game. It initializes game settings, generates the map, places entities, and starts the game loop. It handles player movement, enemy encounters, and displays the game state.

For the complete code, check out the [main.py file](https://github.com/kgordu/linguistic_game/blob/main/main.py) in the repository.

## Contact

Let me know if there are any specific details you’d like to adjust or additional sections you want to include!  
* **Email**: kivancgordu@hotmail.com
* **Version**: 1.0.0
* **Date**: 22-06-2024
