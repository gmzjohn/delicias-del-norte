from decimal import Decimal
from datetime import datetime, timezone

class Product:
    def __init__(
        self,
        id: int, 
        name: str, 
        price: Decimal,
        created_by: int,
        updated_by: int,
        description: str | None = None, 
        active: str = "active",
    ):
        self.id = id
        self.name = name
        self.price = price
        self.created_by = created_by
        self.updated_by = updated_by
        self.description = description
        self.is_active = is_active
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
        