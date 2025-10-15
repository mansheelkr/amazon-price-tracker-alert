# amazon-price-tracker-alert

**Day 47 of 100 Days of Python** — a simple Amazon price tracker that emails you when a product drops below your target price.

---

## Features
- Fetches product title and price from an Amazon product page
- Compares against your `BUY_PRICE`
- Sends an email alert via SMTP when price is below target
- Loads secrets from `.env` (kept out of Git)

## Tech Stack
- Python 3.10+
- `requests`, `beautifulsoup4`
- `python-dotenv`
- `smtplib`

---

## Setup

1. **Clone and enter the project**
   ```bash
   git clone https://github.com/<your-username>/amazon-price-tracker-alert.git
   cd amazon-price-tracker-alert
2. **Create & activate a virtualenv (optional but recommended)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
3. **Install dependencies**
   ```bash
   pip install requests beautifulsoup4 python-dotenv
4. **Create a .env file (do NOT commit this)**
   Put your credentials inside:
   ```ini
   EMAIL_ADDRESS=your_email@example.com
   EMAIL_PASSWORD=your_app_password_or_smtp_password
   SMTP_ADDRESS=smtp.gmail.com
5. **Ensure .env is ignored by Git**
   Create a .gitignore (if not present) and include:
   ```bash
   .env
   __pycache__/
   .venv/

## How It Works
1. The script sends an HTTP GET request to the Amazon product URL and parses the HTML using BeautifulSoup.
2. It extracts:
   - The product title (id="productTitle")
   - The current price (class="a-offscreen")
3. It compares the price to your target BUY_PRICE.
4. If the price is below the threshold, it sends you an email alert with the product name, current price, and link.

## Usage

1. Open the script and update:
   ```python
   live_URL = "https://www.amazon.com/dp/<product-id>"
   BUY_PRICE = 110  # set your target price
2. Run the script
3. If the product price is below your threshold, you’ll receive an email like:
   ```bash
   Subject: Amazon Price Alert!
   Instant Pot Duo 7-in-1 is on sale for $109.99!
   https://www.amazon.com/dp/B075CYMYK6
   
## Troubleshooting
1. AttributeError: 'NoneType' object has no attribute 'getText'
   - The page layout changed or you hit an Amazon bot-protection page.
   - Try adding or updating your User-Agent in the header.
2. Email not sending?
   - Check your .env credentials.
   - For Gmail, create an App Password (you can’t use your normal password if 2FA is on).



   
