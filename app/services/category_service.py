from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.category import Category as CategoryModel
from app.schemas.category import CategoryCreate, CategoryUpdate


def get_category(db: Session, category_id: int) -> Optional[CategoryModel]:
    """Retrieve a single category by ID from the database."""
    return db.query(CategoryModel).filter(CategoryModel.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100) -> List[CategoryModel]:
    """Retrieve all categories from the database with pagination."""
    return db.query(CategoryModel).offset(skip).limit(limit).all()


def create_category(db: Session, category: CategoryCreate) -> CategoryModel:
    """Create a new category in the database."""
    db_category = CategoryModel(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)  # Refresh to get the ID assigned by the DB
    return db_category


def update_category(
    db: Session, category_id: int, category_update: CategoryUpdate
) -> Optional[CategoryModel]:
    """Update an existing category in the database."""
    db_category = get_category(db, category_id)
    if db_category:
        update_data = category_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
    return db_category  # Returns the updated category or None if not found


def delete_category(db: Session, category_id: int) -> Optional[CategoryModel]:
    """Delete a category from the database."""
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category  # Returns the deleted category or None if not found
