from pydantic import BaseModel, Field

class MenuSection(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=50)
    is_active: bool = True