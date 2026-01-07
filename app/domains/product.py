from decimal import Decimal
from datetime import datetime
from product_recipe import ProductRecipe
from base_entity import BaseEntity
from enums.entity_status import EntityStatus

class Product(BaseEntity):
    def __init__(
        self,
        id: int,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
        name: str, 
        price: Decimal,
        recipe_steps: list[ProductRecipe],
        description: str | None = None,
    ):
        super().__init__(
            id = id,
            status = status,
            created_by = created_by,
            updated_by = updated_by,
            created_at = created_at,
            updated_at = updated_at
        )
        self.name = name
        self.price = price
        self.created_by = created_by
        self.updated_by = updated_by
        self.description = description
        self.status = status
        self.recipe_steps = recipe_steps
