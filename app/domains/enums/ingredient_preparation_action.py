from enum import Enum


class IngredientPreparationAction(str, Enum):
    CLEANING = "cleaning"
    CUTTING = "cutting"
    FRYING = "frying"
    BAKING = "baking"
    BOILING = "boiling"
    GRILLED = "grilled"
