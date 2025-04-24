from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    """Schema for creating a new category."""

    pass


class CategoryUpdate(CategoryBase):
    """Schema for updating an existing category."""

    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True  # Or from_attributes = True for Pydantic v2+
