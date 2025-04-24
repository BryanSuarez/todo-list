from typing import List, Optional
from app.schemas.category import Category, CategoryCreate, CategoryUpdate

# In-memory storage for simplicity
categories_db = {}
next_id = 1


def get_categories() -> List[Category]:
    """Retrieve all categories."""
    return list(categories_db.values())


def get_category(category_id: int) -> Optional[Category]:
    """Retrieve a single category by ID."""
    return categories_db.get(category_id)


def create_category(category: CategoryCreate) -> Category:
    """Create a new category."""
    global next_id
    new_category = Category(id=next_id, **category.model_dump())
    categories_db[next_id] = new_category
    next_id += 1
    return new_category


def update_category(
    category_id: int, category_update: CategoryUpdate
) -> Optional[Category]:
    """Update an existing category."""
    if category_id in categories_db:
        stored_category_data = categories_db[category_id]
        update_data = category_update.model_dump(exclude_unset=True)
        updated_category = stored_category_data.model_copy(update=update_data)
        categories_db[category_id] = updated_category
        return updated_category
    return None


def delete_category(category_id: int) -> Optional[Category]:
    """Delete a category."""
    return categories_db.pop(category_id, None)
