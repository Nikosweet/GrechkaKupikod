from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from database.database import Base
from database.models.category import CategoryOrm
from database.models.product import ProductOrm

class ProductCategoryOrm(Base):

    __tablename__ = 'product_categories'

    product_id: Mapped[int] = mapped_column( ForeignKey("products.id"), primary_key=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)

    product: Mapped["ProductOrm"] = relationship(back_populates="category_associations")
    
    category: Mapped["CategoryOrm"] = relationship(back_populates="product_associations")