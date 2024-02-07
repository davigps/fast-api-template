from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    declarative_base,
    mapped_column,
    relationship,
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(nullable=False)
    full_name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    posts: Mapped[List["Post"]] = relationship(back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    image_key: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=True)
    views: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")
    category_id: Mapped[int] = mapped_column(ForeignKey("post_categories.id"))
    category: Mapped["PostCategory"] = relationship(back_populates="posts")


class PostCategory(Base):
    __tablename__ = "post_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    posts: Mapped[List["Post"]] = relationship(back_populates="category")
