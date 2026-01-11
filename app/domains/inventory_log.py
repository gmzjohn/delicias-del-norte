from datetime import datetime

from base_entity import BaseEntity
from enums.entity_status import EntityStatus
from ingredient import Ingredient
from inventory_item import InventoryItem


class InventoryLog(BaseEntity):
    def __init__(
        self,
        id: int,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
        ingredient: Ingredient,
        item: InventoryItem,
        quantity: int,
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
        self.item = item
        self.quantity = quantity
