from sqlalchemy.orm import sessionmaker

from app.database.connection import engine


def get_session():
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
