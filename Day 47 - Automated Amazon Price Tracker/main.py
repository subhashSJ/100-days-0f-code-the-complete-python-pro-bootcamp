import requests
from bs4 import BeautifulSoup
import lxml

flipkart_product_url = "https://www.flipkart.com/apple-2020-macbook-air-m1-8-gb-256-gb-ssd-mac-os-big-sur-mgn93hn-a/p/itm6b02c9a9d9d28?pid=COMFXEKMXWUMGPHW&lid=LSTCOMFXEKMXWUMGPHWKF7Y8O&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_3&otracker=browse&fm=organic&iid=80555bb7-e58d-4212-ba5e-26868158ae66.COMFXEKMXWUMGPHW.SEARCH&ppt=None&ppn=None&ssid=dyzigy7uhs0000001703003926321"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url=flipkart_product_url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find(class_="_30jeq3 _16Jk6d").get_text()
price_without_currency = price.split("₹")[1]
price_as_int = int(price_without_currency.replace(",", ""))
print(price_as_int)

if price_as_int < 75000:
    # send sms
    pass


# You can run this python file everyday (use https://www.pythonanywhere.com/ to host your python file) 
# and when the price is below some threshold then you can send a sms using Twilio to yourself