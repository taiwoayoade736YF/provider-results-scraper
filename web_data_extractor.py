
import requests
from bs4 import BeautifulSoup



def fetch_html(url, max_retries=3):
    """Download a webpage and retry after temporary failures."""
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(
                url,
                timeout=(10, 30),
                headers={"User-Agent": "Mozilla/5.0"},
            )
            response.raise_for_status()
            return response.text

        except requests.RequestException as error:
            print(
                f"Attempt {attempt}/{max_retries} failed: {error}"
            )

            if attempt == max_retries:
                raise

            import time
            time.sleep(2)





def parse_products(html, base_url):
    """Extract book titles, prices, and links from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    products = []

    for item in soup.select("article.product_pod"):
        title_link = item.select_one("h3 a")
        price = item.select_one(".price_color")

        if title_link and price:
            products.append({
                "name": title_link.get("title", title_link.get_text(strip=True)),
                "price": price.get_text(strip=True).replace("Â£", "£"),
                "url": requests.compat.urljoin(
                    base_url, title_link.get("href", "")
                ),
            })

    return products



def remove_duplicates(products):
    """Remove duplicate products."""
    unique_products = []
    seen = set()

    for product in products:
        key = (
            product["name"],
            product["price"],
            product["url"],
        )

        if key not in seen:
            seen.add(key)
            unique_products.append(product)

    return unique_products
