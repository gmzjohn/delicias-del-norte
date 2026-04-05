from datetime import datetime, timezone
from typing import Optional

from app.domains.order import Order
from app.domains.order_item import OrderItem
from app.domains.client import Client
from app.domains.enums.entity_status import EntityStatus
from app.repositories.OrderRepository import OrderRepository


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def create_order(
        self,
        order_id: int,
        client: Client,
        order_items: list[OrderItem],
        created_by: int,
    ) -> Order:
        now = datetime.now(tz=timezone.utc)
        order = Order(
            id=order_id,
            status=EntityStatus.ACTIVE,
            created_by=created_by,
            updated_by=created_by,
            created_at=now,
            updated_at=now,
            order_items=order_items,
            client=client,
        )
        return self._repository.save(order)

    def find_order(self, order_id: int) -> Optional[Order]:
        return self._repository.find(order_id)

    def delete_order(self, order_id: int) -> bool:
        return self._repository.delete(order_id)
