from datetime import datetime
from decimal import Decimal
from typing import List

from .base_entity import BaseEntity
from .enums.entity_status import EntityStatus
from .enums.measure_unit import MeasureUnit
from .enums.product_type import ProductType
from .product_recipe import ProductRecipe


class Product(BaseEntity):
    def __init__(
        self,
        id: int,
        name: str,
        price: Decimal,
        type: ProductType,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
        measure_unit: MeasureUnit,
        description: str | None = None,
        recipe: List[ProductRecipe] | None = None,
    ):
        super().__init__(
            id=id,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
        )

        self.name = name
        self.price = price
        self.type = type
        self.measure_unit = measure_unit
        self.description = description
        self.recipe = recipe
