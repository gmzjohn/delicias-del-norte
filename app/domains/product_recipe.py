from datetime import datetime
from decimal import Decimal
from typing import Optional

from app.utils.linked_list import LinkedList

from .base_entity import BaseEntity
from .enums.entity_status import EntityStatus
from .enums.measure_unit import MeasureUnit
from .preparation_action import PreparationAction
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
        ingredient: Product,
        quantity: Decimal,
        measure_unit: MeasureUnit,
        actions: Optional[LinkedList[PreparationAction]] = None,
    ):
        super().__init__(
            id=id,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
        )
        self.ingredient = ingredient
        self.quantity = quantity
        self.measure_unit = measure_unit
        self.actions = actions
