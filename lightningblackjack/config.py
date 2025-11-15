import os

# Casino LNURL for payments
CASINO_LNURL = os.getenv(
    "LIGHTNINGBLACKJACK_CASINO_LNURL",
    "lnurl1dp68gurn8ghj7ampd3kx2ar0veekzar0wd5xjtnrdakj7tnhv4kxctttdehhwm30d3h82unvwqhhx6tvv4u8qetjd9jkucm9xgcsmep3s3"
)

# Minimum bet and entry amounts in sats
MIN_ENTRY_AMOUNT = 2100
MIN_BET_AMOUNT = 210
