from datetime import datetime
from .base_entity import BaseEntity
from .enums.entity_status import EntityStatus
from .order_item import OrderItem
from .client import Client


class Order(BaseEntity):
    def __init__(
        self,
        id: int,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
        order_items: list[OrderItem],
        client: Client,
    ):
        super().__init__(
            id=id,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
        )
        self.order_items = order_items
        self.client = client
