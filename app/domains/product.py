from datetime import datetime
from decimal import Decimal

from .base_entity import BaseEntity
from .enums.entity_status import EntityStatus
from .enums.product_type import ProductType


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
        description: str | None = None,
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
        self.description = description
