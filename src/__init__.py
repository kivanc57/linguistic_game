from config.constants import (
  HEALTH_CONSTANT, SIZE_CONSTANT, AMOUNT_CONSTANTS,
  ENTITY_CONSTANTS, SPATIAL_CONSTANTS, TEXT_DIR, TEXT_F_NAME
)

from src.gameplay import print_game, count_enemies
from src.map_utils import get_map, read_print_intro, enumerate_amounts, place_entities
from src.mechanics import make_movement
import logging

logging.basicConfig(
  level=logging.INFO,
  filename='src.log',
  filemode='a',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Package is initialized")


__version__ = "1.0.0"
__date__ = "22-07-2024"
__email__ = "kivancgordu@hotmail.com"
__status__ = "production"

__all__ = [
  'make_movement', 'print_game', 'count_enemies',
  'get_map', 'enumerate_amounts', 'place_entities', 'read_print_intro',
  'HEALTH_CONSTANT', 'SIZE_CONSTANT', 'AMOUNT_CONSTANTS', 'ENTITY_CONSTANTS',
  'SPATIAL_CONSTANTS', 'TEXT_DIR', 'TEXT_F_NAME'
  ]
  
