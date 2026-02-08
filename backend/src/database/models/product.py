from sqlalchemy import  String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.database import Base
from database.models.category import CategoryOrm
from database.models.product_categories import ProductCategoryOrm
class ProductOrm(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)

    category_associations: Mapped[List["ProductCategoryOrm"]] = relationship(
        back_populates="product", 
        cascade="all, delete-orphan"
    )

    @property
    def categories(self) -> List["CategoryOrm"]:
        return [assoc.category for assoc in self.category_associations]


    