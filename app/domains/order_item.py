from datetime import datetime
from decimal import Decimal

from .base_entity import BaseEntity
from .employee import Employee
from .enums.entity_status import EntityStatus
from .order import Order
from .product import Product


class OrderItem(BaseEntity):
    def __init__(
        self,
        id: int,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
        product: Product,
        quantity: int,
        price: Decimal,
        order: Order,
        assigned_chef: Employee,
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
        self.quantity = quantity
        self.price = price
        self.order = order
        self.assigned_chef = assigned_chef
