from fastapi import APIRouter
from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_lightningblackjack")

lightningblackjack_ext: APIRouter = APIRouter(
    prefix="/lightningblackjack", tags=["lightningblackjack"]
)


def lightningblackjack_renderer():
    return template_renderer(["lightningblackjack/templates"])


from .views import *  # noqa: F401,F403
from .views_api import *  # noqa: F401,F403
