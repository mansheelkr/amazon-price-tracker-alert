from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

#practice_URL = "https://appbrewery.github.io/instant_pot/"
live_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(url=live_URL, headers=os.getenv("header"))
amazon_webpage = response.content

soup = BeautifulSoup(amazon_webpage, "html.parser")
#print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").getText()

# Remove the dollar sign using split
price_without_currency = price.split("$")

# Convert to floating point number
price = float(price_without_currency[1])
print(price)

# ====================== Send an Email ===========================

# Get the product title
title = soup.find(id="productTitle").getText().strip()

# Set the price below which you would like to get a notification
BUY_PRICE = 110

if price < BUY_PRICE:
  message = f"{title} is on sale for ${price}!"

  with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587) as connection:
    connection.starttls()
    connection.login(user=os.getenv("EMAIL_ADDRESS"), password=os.getenv("EMAIL_PASSWORD"))
    connection.sendmail(
      from_addr=os.getenv("EMAIL_ADDRESS"), 
      to_addrs='mansheelrandhawa2001@gmail.com', 
      msg=f"Subject:Amazon Price Alert!\n\n{message}\n{live_URL}".encode("utf-8")
    )
