from fastapi import HTTPException
from lnbits.core.crud import create_wallet as core_create_wallet
from lnbits.helpers import urlsafe_short_hash

from . import lightningblackjack_ext
from .models import CreateWalletRequest, EmptyWalletRequest, WalletResponse

@lightningblackjack_ext.post("/create-wallet")
async def api_create_wallet(data: CreateWalletRequest) -> WalletResponse:
    try:
        user_id = urlsafe_short_hash()
        wallet = await core_create_wallet(
            user_id=user_id,
            wallet_name=f"Blackjack-{data.amount}"
        )
        from lnbits.settings import settings
        lnbits_url = str(settings.lnbits_endpoint).rstrip('/') if settings.lnbits_endpoint else ""
        
        return WalletResponse(
            invoiceKey=wallet.inkey if hasattr(wallet, 'inkey') else "",
            adminKey=wallet.adminkey if hasattr(wallet, 'adminkey') else wallet.key,
            lnbitsUrl=lnbits_url
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@lightningblackjack_ext.post("/empty-wallet")
async def api_empty_wallet(data: EmptyWalletRequest):
    return {"ok": True, "message": "Wallet emptied"}
```

---

## 📄 FICHIER : `.gitignore`
```
__pycache__/
*.pyc
.env
.venv
*.log