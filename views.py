from fastapi import Request
from fastapi.responses import HTMLResponse

from . import lightningblackjack_ext, lightningblackjack_renderer
from .config import CASINO_LNURL

@lightningblackjack_ext.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return lightningblackjack_renderer().TemplateResponse(
        "lightningblackjack/index.html",
        {"request": request, "casino_lnurl": CASINO_LNURL}
    )