from Base import Base
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column


class ReactionRoleMessage(Base):
    __tablename__ = "reaction_role_msg"
    message_id: Mapped[str] = mapped_column(primary_key=True)
    text: Mapped[str]
    reaction_role_mapping: Mapped[dict[str, str]] = mapped_column(JSON, default={})
