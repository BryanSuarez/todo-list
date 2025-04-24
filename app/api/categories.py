from fastapi import APIRouter, HTTPException, status
from typing import List

from app.schemas.category import Category, CategoryCreate, CategoryUpdate
from app.services import category_service

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_new_category(category: CategoryCreate):
    """Create a new category."""
    return category_service.create_category(category=category)


@router.get("/", response_model=List[Category])
def read_categories():
    """Retrieve all categories."""
    return category_service.get_categories()


@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int):
    """Retrieve a specific category by ID."""
    db_category = category_service.get_category(category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.put("/{category_id}", response_model=Category)
def update_existing_category(category_id: int, category: CategoryUpdate):
    """Update a category."""
    updated_category = category_service.update_category(
        category_id=category_id, category_update=category
    )
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category


@router.delete("/{category_id}", response_model=Category)
def delete_existing_category(category_id: int):
    """Delete a category."""
    deleted_category = category_service.delete_category(category_id=category_id)
    if deleted_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category
