from fastapi import APIRouter, Depends

from app.controllers.deps import get_session_controller
from app.controllers.session import SessionController
from app.schemas.sessions import LoginPayload, LoginView

sessions = APIRouter()


@sessions.post(
    "/sessions",
    tags=["sessions"],
    response_model=LoginView,
    description="Return JWT Token and User information",
)
def make_login(
    body: LoginPayload,
    controller: SessionController = Depends(get_session_controller),
):
    return controller.login(body.email, body.password)
