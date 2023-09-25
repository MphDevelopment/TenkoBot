from Base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Forum(Base):
    __tablename__ = "forum"
    channel_id: Mapped[str] = mapped_column(primary_key=True)
    forum_cat: Mapped[str] = mapped_column(ForeignKey("forum_category.category_id"))
    topic: Mapped[str]
    role_id: Mapped[str]
    reaction: Mapped[str]
