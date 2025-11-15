from pydantic import BaseModel

class CreateWalletRequest(BaseModel):
    amount: int

class EmptyWalletRequest(BaseModel):
    adminKey: str
    amount: int
    lnurl: str

class WalletResponse(BaseModel):
    invoiceKey: str
    adminKey: str
    lnbitsUrl: str