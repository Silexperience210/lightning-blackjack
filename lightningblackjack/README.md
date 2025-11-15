# Lightning Blackjack - Extension LNbits

Un jeu de Blackjack utilisant Bitcoin Lightning Network via LNbits.

## Installation

### Méthode 1 : Installation via l'interface LNbits (recommandé)

1. Connectez-vous à votre instance LNbits en tant qu'administrateur
2. Allez dans **Extensions** → **Manage Extensions**
3. Dans la section "Install Extension", collez l'URL de ce dépôt GitHub :
   ```
   https://github.com/Silexperience210/lightning-blackjack
   ```
4. Cliquez sur **Install**

### Méthode 2 : Installation manuelle

1. Clonez ce dépôt dans le dossier des extensions LNbits :
   ```bash
   cd /path/to/lnbits/lnbits/extensions/
   git clone https://github.com/Silexperience210/lightning-blackjack.git lightningblackjack
   ```

2. Redémarrez LNbits :
   ```bash
   systemctl restart lnbits
   # ou
   poetry run lnbits
   ```

3. Activez l'extension dans l'interface LNbits

## Configuration

### Variables d'environnement

Vous pouvez configurer l'extension avec les variables suivantes dans votre fichier `.env` :

```bash
# LNURL du casino pour recevoir les paiements
LIGHTNINGBLACKJACK_CASINO_LNURL=lnurl1dp68gurn8ghj7ampd3kx2ar0veekzar0wd5xjtnrdakj7tnhv4kxctttdehhwm30d3h82unvwqhhx6tvv4u8qetjd9jkucm9xgcsmep3s3
```

## Utilisation

1. Accédez à l'extension via : `https://votre-instance-lnbits.com/lightningblackjack/`
2. Entrez le montant souhaité (minimum 2100 sats)
3. Payez la facture Lightning générée
4. Jouez au Blackjack !

## Règles du jeu

- **Mise minimale** : 210 sats
- **Montant d'entrée minimum** : 2100 sats
- Le joueur peut :
  - **CARTE** : Tirer une carte supplémentaire
  - **RESTER** : Garder sa main actuelle
- Le croupier tire jusqu'à avoir au moins 17
- **Blackjack** (As + figure) paie 2.5x la mise
- **Victoire** paie 2x la mise
- **Égalité** rembourse la mise

## Fonctionnalités

- ✅ Paiement via Lightning Network
- ✅ Création automatique de wallet temporaire
- ✅ Retrait des gains
- ✅ Interface responsive et moderne
- ✅ QR codes pour les factures

## Architecture

L'extension est composée de :

- `__init__.py` : Initialisation de l'extension
- `views.py` : Routes pour l'interface web
- `views_api.py` : API endpoints
- `models.py` : Modèles de données Pydantic
- `config.py` : Configuration
- `templates/` : Templates HTML Jinja2
- `manifest.json` : Métadonnées de l'extension

## Sécurité

⚠️ **Important** : Cette extension crée des wallets temporaires pour chaque session de jeu. Assurez-vous de configurer correctement votre LNURL de casino pour recevoir les paiements.

## Licence

MIT

## Support

Pour toute question ou problème, ouvrez une issue sur GitHub.
