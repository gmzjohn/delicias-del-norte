from datetime import datetime
from decimal import Decimal

from .base_entity import BaseEntity
from .enums.entity_status import EntityStatus
from .enums.measure_unit import MeasureUnit
from .enums.ingredient_preparation_action import IngredientPreparationAction
from .product import Product


class ProductRecipe(BaseEntity):
    def __init__(
        self,
        id: int,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
        product: Product,
        ingredient: Product,
        quantity: Decimal,
        measure_unit: MeasureUnit,
        action: IngredientPreparationAction,
        estimated_time: int,
    ):
        super().__init__(
            id=id,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
        )
        self.product = product
        self.ingredient = ingredient
        self.quantity = quantity
        self.measure_unit = measure_unit
        self.action = action
        self.estimated_time = estimated_time
