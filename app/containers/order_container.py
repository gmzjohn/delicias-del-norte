from datetime import datetime

from app.domains.enums.entity_status import EntityStatus

from app.domains.order import Order
from app.domains.client import Client
from app.domains.order_item import OrderItem


class OrderContainer:
    def __init__(self) -> None:
        self._order: Order | None = None

    def create_order(
        self,
        id: int,
        client: Client,
        created_by: int,
        updated_by: int,
        order_items: list[OrderItem],
        status: EntityStatus,
        created_at: datetime,
        updated_at: datetime,
    ) -> Order:
        if self._order is not None:
            raise RuntimeError("An active Order already exists in this container ")

        order = Order(
            id=id,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
            order_items=order_items,
            client=client,
        )
        self._order = order

        return order

    def get_order(self) -> Order | None:
        return self._order
