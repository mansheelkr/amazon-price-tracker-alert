from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

#practice_URL = "https://appbrewery.github.io/instant_pot/"
live_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
#header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": '__gads=ID=7b6971f347d8bd41:T=1760565361:RT=1760565361:S=ALNI_MZT71-Ma-GPqm4ytzeXwSWdqPup4Q; __gpi=UID=0000129ed3cd0793:T=1760565361:RT=1760565361:S=ALNI_MbIpUGiQ6YdGuPcnSXc1TaSEAa-7w; __eoi=ID=2299d82db7c60040:T=1760565361:RT=1760565361:S=AA-Afja1FvHPL-aSNSf5mLUpqBx5; FCNEC=%5B%5B%22AKsRol_XwkfnMega-PuQvhAV7kZeU3dP52U3QxrHTpN4AtmaBu25pU51h8D7qu7Xe8KIBmd3z6VXmOza8s3FCIuf4mH9SsTgDIZmQpe_h1TH4AJUAnTFeFF2VstYEKY-vpShrZqZ0WCGXraUsVMdaR1KsMX6d2gLAQ%3D%3D%22%5D%5D',
    "Priority": "u=0, i",
    "Referer": live_URL,
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.get(url=live_URL, headers=header)
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
