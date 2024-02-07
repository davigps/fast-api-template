from fastapi import Depends

from app.controllers.post import PostController
from app.controllers.post_category import PostCategoryController
from app.controllers.session import SessionController
from app.controllers.user import UserController
from app.models import Post, PostCategory, User
from app.repositories.deps import (
    get_post_category_repository,
    get_post_repository,
    get_user_repository,
)
from app.repositories.post import PostRepository
from app.repositories.post_category import PostCategoryRepository
from app.repositories.user import UserRepository
from app.services.bucket_manager import BucketManager


def get_user_controller(
    repository: UserRepository = Depends(get_user_repository),
):
    return UserController(User, repository)


def get_session_controller(
    user_repository: UserRepository = Depends(get_user_repository),
):
    return SessionController(user_repository)


def get_post_category_controller(
    repository: PostCategoryRepository = Depends(get_post_category_repository),
):
    return PostCategoryController(PostCategory, repository)


def get_post_controller(
    repository: PostRepository = Depends(get_post_repository),
):
    return PostController(Post, repository, BucketManager())
