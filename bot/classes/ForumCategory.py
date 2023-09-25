from Base import Base
from typing import List
from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ForumCategory(Base):
    __tablename__ = "forum_category"

    category_id: Mapped[str] = mapped_column(primary_key=True)
    forums: Mapped[List["Forum"]] = relationship(cascade="all, delete-orphan")
    description_message_id: Mapped["str"] = mapped_column(
        ForeignKey("reaction_role_msg.message_id")
    )
