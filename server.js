const express = require('express');
const fetch = require('node-fetch');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, '..'))); // Sert index.html

const LNBITS = "https://legend.lnbits.com"; // TON LNbits
const ADMIN_KEY = "TA_CLÉ_ADMIN_PRINCIPALE"; // SÉCURISÉE ICI
const CASINO_LNURL = "lnurl1dp68gurn8ghj7ampd3kx2ar0veekzar0wd5xjtnrdakj7tnhv4kxctttdehhwm30d3h82unvwqhhx6tvv4u8qetjd9jkucm9xgcsmep3s3";

app.post('/create-wallet', async (req, res) => {
    try {
        const wallet = await fetch(`${LNBITS}/api/v1/wallet`, {
            method: 'POST',
            headers: { 'X-Api-Key': ADMIN_KEY, 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: `Session ${Date.now()}` })
        }).then(r => r.json());
        res.json({ invoiceKey: wallet.inkey, adminKey: wallet.adminkey, lnbitsUrl: LNBITS });
    } catch (e) { res.status(500).json({ error: 'LNbits error' }); }
});

app.post('/empty-wallet', async (req, res) => {
    const { adminKey, amount, lnurl } = req.body;
    try {
        await fetch(`${LNBITS}/api/v1/payments`, {
            method: 'POST',
            headers: { 'X-Api-Key': adminKey, 'Content-Type': 'application/json' },
            body: JSON.stringify({ out: true, amount, lnurl, memo: 'Casino win' })
        });
        res.json({ ok: true });
    } catch (e) { res.status(500).json({ error: 'Payment failed' }); }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Casino ON ${PORT}`));
