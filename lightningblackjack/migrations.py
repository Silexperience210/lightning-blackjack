"""
Lightning Blackjack migrations
"""

# No database tables needed for this extension
# All game state is stored client-side
# Wallets are created dynamically via LNbits core API

async def m001_initial(db):
    """
    Initial migration - no tables needed for this extension.
    Game logic runs client-side, wallet management uses LNbits core.
    """
    pass
