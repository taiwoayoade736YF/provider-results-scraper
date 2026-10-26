
import csv
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from web_data_extractor import (
    fetch_html,
    parse_products,
    remove_duplicates,
)


base_url = "https://books.toscrape.com/"
current_url = base_url
all_books = []

while current_url:
    print(f"Scraping: {current_url}")

    html = fetch_html(current_url)
    books = parse_products(html, current_url)
    all_books.extend(books)

    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")

    if next_link:
        current_url = urljoin(current_url, next_link["href"])
    else:
        current_url = None

all_books = remove_duplicates(all_books)

with open(
    "books.csv",
    "w",
    newline="",
    encoding="utf-8-sig",
) as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "price", "url"],
    )
    writer.writeheader()
    writer.writerows(all_books)

print(f"\nBooks collected: {len(all_books)}")
print("Data saved to books.csv")


