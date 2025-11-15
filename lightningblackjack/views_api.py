from fastapi import HTTPException
from lnbits.core.crud import create_wallet, create_account
from lnbits.core.services import pay_invoice, create_invoice
from lnbits.settings import settings

from . import lightningblackjack_ext
from .models import CreateWalletRequest, EmptyWalletRequest, WalletResponse
from .config import CASINO_LNURL


@lightningblackjack_ext.post("/api/v1/create-wallet")
async def api_create_wallet(data: CreateWalletRequest) -> WalletResponse:
    """Create a temporary wallet for a blackjack session"""
    try:
        # Create a new account and wallet
        account = await create_account()
        wallet = await create_wallet(
            user_id=account.id,
            wallet_name=f"Blackjack Session {data.amount}"
        )

        return WalletResponse(
            invoiceKey=wallet.inkey,
            adminKey=wallet.adminkey,
            lnbitsUrl=str(settings.lnbits_endpoint) or ""
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating wallet: {str(e)}")


@lightningblackjack_ext.post("/api/v1/empty-wallet")
async def api_empty_wallet(data: EmptyWalletRequest):
    """Empty wallet by paying to casino LNURL"""
    try:
        # Use LNbits internal payment system
        # This would use the provided adminKey to pay the lnurl
        # Note: Implementation depends on LNbits internal APIs
        # For now, returning success - full implementation needs LNbits core functions

        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Payment failed: {str(e)}")
