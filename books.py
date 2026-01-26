import requests
from bs4 import BeautifulSoup

GBP_TO_UAH = 50

url = "http://books.toscrape.com/"

while url:
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.select(".product_pod"):
        price_text = book.select_one(".price_color").text
        price_gbp = float(price_text.replace("£", ""))
        price_uah = price_gbp * GBP_TO_UAH
        print(f"{price_uah:.2f} грн")

    next_page = soup.select_one("li.next a")
    if next_page:
        url = "http://books.toscrape.com/" + next_page["href"]
    else:
        url = None
