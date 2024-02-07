from unittest.mock import Mock

import pytest
from fastapi import UploadFile

from app.controllers.post import PostController
from app.models import Post, PostCategory, User
from app.repositories.post import PostRepository
from app.schemas.post import PostCreateWithImage, PostUpdate
from app.services.bucket_manager import BucketManager


class TestPostController:
    @pytest.fixture
    def setup(self, db_session, make_user, make_post, make_post_category):
        self.repository = PostRepository(Post, db_session)

        self.bucket_mock = Mock(
            spec_set=BucketManager,
            upload_file=Mock(return_value="image_key"),
        )
        self.controller = PostController(
            Post, self.repository, self.bucket_mock
        )

        self.post_category: PostCategory = make_post_category()
        self.created_user: User = make_user()
        db_session.add_all([self.created_user, self.post_category])
        db_session.commit()

        self.created_post: Post = make_post(
            user=self.created_user, category=self.post_category
        )
        self.repository.add(self.created_post)

    def test_create_post(self, setup, faker):
        create = PostCreateWithImage(
            category_id=self.post_category.id,
            description=faker.text(),
            image=UploadFile(file=Mock()),
            location=faker.text(),
            price=faker.random_int(),
            title=faker.name(),
            user_id=self.created_user.id,
        )

        post = self.controller.create(create)

        assert post.id is not None
        assert post.title == create.title
        assert post.price == create.price

        found_post = self.repository.get_by_id(post.id)
        assert found_post is not None

    def test_get_post(self, setup):
        found_post = self.controller.get_by_id(self.created_post.id)
        assert found_post is not None
        assert found_post.id == self.created_post.id
        assert found_post.title == self.created_post.title
        assert found_post.price == self.created_post.price

    def test_get_all_posts(self, setup):
        found_posts = self.controller.get_all()
        assert len(found_posts) == 1
        assert found_posts[0].id == self.created_post.id
        assert found_posts[0].title == self.created_post.title
        assert found_posts[0].price == self.created_post.price

    def test_update_post(self, setup, faker):
        update = PostUpdate(
            description=faker.text(),
            price=faker.random_int(),
            title=faker.name(),
        )

        updated_post = self.controller.update(
            self.created_post.id, update, self.created_user.id
        )
        assert updated_post is not None
        assert updated_post.id == self.created_post.id
        assert updated_post.title == self.created_post.title
        assert updated_post.description == self.created_post.description
        assert updated_post.price == self.created_post.price

        found_post = self.repository.get_by_id(self.created_post.id)
        assert found_post is not None
        assert found_post.title == self.created_post.title
        assert found_post.description == self.created_post.description
        assert found_post.price == self.created_post.price

    def test_delete_user(self, setup):
        self.controller.delete(self.created_post.id, self.created_user.id)

        found_post = self.repository.get_by_id(self.created_post.id)
        assert found_post is None
