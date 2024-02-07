from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.deps import get_session
from app.models import Post, PostCategory, User
from app.repositories.post import PostRepository
from app.repositories.post_category import PostCategoryRepository
from app.repositories.user import UserRepository


def get_user_repository(session: Session = Depends(get_session)):
    return UserRepository(User, session)


def get_post_category_repository(session: Session = Depends(get_session)):
    return PostCategoryRepository(PostCategory, session)


def get_post_repository(session: Session = Depends(get_session)):
    return PostRepository(Post, session)
