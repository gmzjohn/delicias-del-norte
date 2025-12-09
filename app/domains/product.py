from decimal import Decimal
from datetime import datetime, timezone
from .enums import ProductStatus

class Product:
    def __init__(
        self,
        id: int, 
        name: str, 
        price: Decimal,
        status: ProductStatus,
        created_by: int,
        updated_by: int,
        description: str | None = None,
    ):
        self.id = id
        self.name = name
        self.price = price
        self.created_by = created_by
        self.updated_by = updated_by
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
