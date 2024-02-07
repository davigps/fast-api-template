import pytest

from app.models import Post, PostCategory, User


@pytest.fixture
def make_user(faker):
    def _make_user(**kwargs):
        defaults = dict(
            email=faker.email(),
            full_name=faker.name(),
            password=faker.password(),
            phone="83940028922",
        )

        return User(**{**defaults, **kwargs})

    return _make_user


@pytest.fixture
def make_post(faker):
    def _make_post(user: User, category: PostCategory, **kwargs):
        defaults = dict(
            title=faker.name(),
            image_key=faker.text(),
            description=faker.text(),
            location=faker.text(),
            price=faker.random_int(),
            views=faker.random_int(),
            user=user,
            category=category,
        )

        return Post(**{**defaults, **kwargs})

    return _make_post


@pytest.fixture
def make_post_category(faker):
    def _make_post_category(**kwargs):
        defaults = dict(
            name=faker.name(),
        )

        return PostCategory(**{**defaults, **kwargs})

    return _make_post_category
