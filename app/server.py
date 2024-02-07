from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.post_categories import (
    post_categories as post_categories_router,
)
from app.routes.posts import posts as posts_router
from app.routes.sessions import sessions as sessions_router
from app.routes.users import users as users_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(sessions_router)
app.include_router(post_categories_router)
app.include_router(posts_router)
