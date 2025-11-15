from fastapi import Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from . import lightningblackjack_ext, lightningblackjack_renderer
from .config import CASINO_LNURL

templates = Jinja2Templates(directory="lightningblackjack/templates")


@lightningblackjack_ext.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return lightningblackjack_renderer().TemplateResponse(
        "lightningblackjack/index.html",
        {
            "request": request,
            "casino_lnurl": CASINO_LNURL,
        },
    )
