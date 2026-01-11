from datetime import datetime

from enums.entity_status import EntityStatus
from inventory_item import InventoryItem


class Ingredient(InventoryItem):
    def __init__(
        self,
        id: int,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
        name: str,
        price: int,
    ):
        super().__init__(
            id=id,
            name=name,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
        )
        self.price = price
