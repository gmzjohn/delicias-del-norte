from typing import Optional
from app.domains.order import Order


class OrderRepository:
    def __init__(self) -> None:
        self._store: dict[int, Order] = {}

    def save(self, order: Order) -> Order:
        self._store[order.id] = order
        return order

    def find(self, order_id: int) -> Optional[Order]:
        return self._store.get(order_id)

    def delete(self, order_id: int) -> bool:
        if order_id in self._store:
            del self._store[order_id]
            return True
        return False
