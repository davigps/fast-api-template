import time
from random import choice

from faker import Faker
from sqlalchemy.orm import Session, sessionmaker

from app.database.connection import engine
from app.hashing import Hasher
from app.models import Post, PostCategory, User

faker = Faker(locale="pt_BR")


def get_db_session():
    SessionLocal = sessionmaker(bind=engine)
    engine.echo = False
    session = SessionLocal()

    return session


def clear_all_tables(session: Session):
    session.query(Post).delete()
    session.query(PostCategory).delete()
    session.query(User).delete()

    session.commit()


def create_users(session: Session):
    user = User(
        full_name="John Doe",
        email="usuario@email.com",
        phone="123456789",
        password=Hasher.get_password_hash("12345678"),
    )
    session.add(user)

    for _ in range(10):
        user = User(
            full_name=faker.name(),
            email=faker.email(),
            phone=faker.msisdn(),
            password=faker.password(),
        )

        session.add(user)
    session.commit()


def create_post_categories(session: Session):
    for _ in range(10):
        post_category = PostCategory(
            name=faker.text(max_nb_chars=10),
        )

        session.add(post_category)
    session.commit()


def create_posts(session: Session):
    for _ in range(10):
        users = session.query(User).all()
        user = choice(users)

        categories = session.query(PostCategory).all()
        category = choice(categories)

        post = Post(
            title=faker.text(max_nb_chars=30),
            image_key=faker.text(max_nb_chars=30),
            description=faker.text(max_nb_chars=200),
            location=faker.text(max_nb_chars=30),
            price=faker.pyint(min_value=0, max_value=1000),
            views=faker.pyint(min_value=0, max_value=1000),
            user_id=user.id,
            category_id=category.id,
        )

        session.add(post)
    session.commit()


def main():
    answer = input(
        (
            "This will clear all tables and seed the database."
            " Are you sure? (y/N) "
        )
    )
    if answer.lower() != "y":
        print("Aborting...")
        return

    duration = time.time()
    session = get_db_session()

    print("Clearing all tables...")
    clear_all_tables(session)

    print("Creating users...")
    create_users(session)

    print("Creating post categories...")
    create_post_categories(session)

    print("Creating posts...")
    create_posts(session)

    session.close()

    duration = time.time() - duration
    print(f"Done in {duration:.2f} seconds!")


if __name__ == "__main__":
    main()
